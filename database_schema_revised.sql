-- Revised Database Schema for Housing Price Analysis App
-- PostgreSQL schema for Boulder County housing market analysis
-- REMOVED: All realtor-related tables and functionality

-- =====================================================
-- CORE TABLES
-- =====================================================

-- Properties table (from rentcast.io property data)
CREATE TABLE properties (
    id VARCHAR(255) PRIMARY KEY, -- RentCast property identifier
    formatted_address TEXT,
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    county VARCHAR(100),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    property_type VARCHAR(50),
    property_sub_type VARCHAR(50),
    bedrooms INTEGER,
    bathrooms DECIMAL(4, 1),
    square_footage INTEGER,
    lot_size INTEGER,
    year_built INTEGER,
    garage_spaces INTEGER,
    parking_spaces INTEGER,
    pool BOOLEAN,
    spa BOOLEAN,
    fireplace BOOLEAN,
    central_air BOOLEAN,
    heating_type VARCHAR(50),
    cooling_type VARCHAR(50),
    roof_type VARCHAR(50),
    exterior_type VARCHAR(50),
    flooring_type VARCHAR(50),
    appliances TEXT,
    last_sale_date DATE,
    last_sale_price INTEGER,
    last_seen DATE,
    listed_date DATE,
    status VARCHAR(20), -- active, sold, pending, etc.
    rent_zestimate INTEGER,
    zestimate INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Historical transactions (from Boulder County data)
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    parcel_number VARCHAR(50),
    property_address TEXT,
    city VARCHAR(100),
    sale_date DATE,
    sale_price INTEGER,
    grantor TEXT, -- Seller name
    grantee TEXT, -- Buyer name
    bedrooms INTEGER,
    full_baths INTEGER,
    three_quarter_baths INTEGER,
    half_baths INTEGER,
    above_ground_sqft INTEGER,
    finished_basement_sqft INTEGER,
    unfinished_basement_sqft INTEGER,
    garage_sqft INTEGER,
    finished_garage_sqft INTEGER,
    year_built INTEGER,
    land_value INTEGER,
    building_value INTEGER,
    extra_feature_value INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Property listings (from rentcast.io listings data)
CREATE TABLE listings (
    id VARCHAR(255) PRIMARY KEY, -- RentCast listing identifier
    property_id VARCHAR(255) REFERENCES properties(id),
    list_price INTEGER,
    list_date DATE,
    status VARCHAR(20), -- active, pending, sold, etc.
    days_on_market INTEGER,
    price_history JSONB, -- Array of price changes
    description TEXT,
    photos JSONB, -- Array of photo URLs
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Market trends (aggregated by zip code)
CREATE TABLE market_trends (
    id SERIAL PRIMARY KEY,
    zip_code VARCHAR(10),
    date DATE,
    data_source VARCHAR(50), -- 'rentcast' or 'boulder_county'
    avg_price INTEGER,
    median_price INTEGER,
    price_per_sqft DECIMAL(10, 2),
    days_on_market INTEGER,
    inventory_count INTEGER,
    sales_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(zip_code, date, data_source)
);

-- Zillow market data (static monthly data)
CREATE TABLE zillow_market_data (
    id SERIAL PRIMARY KEY,
    geographic_level VARCHAR(20), -- 'zip_code', 'metro', 'region', 'national'
    geographic_id VARCHAR(50), -- zip code, metro code, region name, etc.
    date DATE,
    data_type VARCHAR(50), -- 'zhvi', 'zri', 'inventory', etc.
    value DECIMAL(15, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(geographic_level, geographic_id, date, data_type)
);

-- ML model data
CREATE TABLE ml_models (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100),
    model_type VARCHAR(50), -- 'regression', 'classification', etc.
    model_version VARCHAR(20),
    model_file_path TEXT,
    training_date DATE,
    accuracy_score DECIMAL(5, 4),
    feature_importance JSONB,
    hyperparameters JSONB,
    is_active BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Model predictions
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    property_id VARCHAR(255) REFERENCES properties(id),
    model_id INTEGER REFERENCES ml_models(id),
    predicted_price INTEGER,
    confidence_score DECIMAL(5, 4),
    feature_values JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User preferences (for property matching)
CREATE TABLE user_preferences (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255), -- Will be implemented when auth is added
    min_price INTEGER,
    max_price INTEGER,
    min_bedrooms INTEGER,
    max_bedrooms INTEGER,
    min_bathrooms DECIMAL(4, 1),
    max_bathrooms DECIMAL(4, 1),
    min_sqft INTEGER,
    max_sqft INTEGER,
    preferred_cities TEXT[], -- Array of city names
    preferred_zip_codes TEXT[], -- Array of zip codes
    must_have_features TEXT[], -- Array of required features
    nice_to_have_features TEXT[], -- Array of preferred features
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Property matches (results of user preference matching)
CREATE TABLE property_matches (
    id SERIAL PRIMARY KEY,
    user_preference_id INTEGER REFERENCES user_preferences(id),
    property_id VARCHAR(255) REFERENCES properties(id),
    match_score DECIMAL(5, 4),
    price_difference INTEGER, -- Difference from user's price range
    feature_match_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- INDEXES FOR PERFORMANCE
-- =====================================================

-- Properties indexes
CREATE INDEX idx_properties_zip_code ON properties(zip_code);
CREATE INDEX idx_properties_city ON properties(city);
CREATE INDEX idx_properties_bedrooms ON properties(bedrooms);
CREATE INDEX idx_properties_price_range ON properties(zestimate) WHERE zestimate IS NOT NULL;
CREATE INDEX idx_properties_location ON properties(latitude, longitude);

-- Transactions indexes
CREATE INDEX idx_transactions_sale_date ON transactions(sale_date);
CREATE INDEX idx_transactions_zip_code ON transactions(property_address);
CREATE INDEX idx_transactions_price ON transactions(sale_price);

-- Listings indexes
CREATE INDEX idx_listings_property_id ON listings(property_id);
CREATE INDEX idx_listings_status ON listings(status);
CREATE INDEX idx_listings_price ON listings(list_price);

-- Market trends indexes
CREATE INDEX idx_market_trends_zip_date ON market_trends(zip_code, date);

-- Predictions indexes
CREATE INDEX idx_predictions_property_id ON predictions(property_id);
CREATE INDEX idx_predictions_model_id ON predictions(model_id);

-- =====================================================
-- TRIGGERS FOR AUTOMATIC TIMESTAMP UPDATES
-- =====================================================

CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_properties_updated_at BEFORE UPDATE ON properties
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_listings_updated_at BEFORE UPDATE ON listings
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_user_preferences_updated_at BEFORE UPDATE ON user_preferences
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- =====================================================
-- VIEWS FOR COMMON QUERIES
-- =====================================================

-- Fair price calculation view (median of comparable properties)
CREATE VIEW fair_prices AS
SELECT 
    p.id,
    p.formatted_address,
    p.bedrooms,
    p.bathrooms,
    p.square_footage,
    p.zip_code,
    p.zestimate,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY p2.zestimate) as fair_price,
    COUNT(p2.id) as comparable_count
FROM properties p
LEFT JOIN properties p2 ON 
    p2.zip_code = p.zip_code 
    AND p2.bedrooms BETWEEN p.bedrooms - 1 AND p.bedrooms + 1
    AND p2.bathrooms BETWEEN p.bathrooms - 0.5 AND p.bathrooms + 0.5
    AND p2.square_footage BETWEEN p.square_footage * 0.8 AND p.square_footage * 1.2
    AND p2.id != p.id
WHERE p.zestimate IS NOT NULL
GROUP BY p.id, p.formatted_address, p.bedrooms, p.bathrooms, p.square_footage, p.zip_code, p.zestimate;

-- Market summary view
CREATE VIEW market_summary AS
SELECT 
    zip_code,
    COUNT(*) as total_properties,
    AVG(zestimate) as avg_price,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY zestimate) as median_price,
    AVG(price_per_sqft) as avg_price_per_sqft,
    COUNT(CASE WHEN status = 'active' THEN 1 END) as active_listings
FROM properties p
LEFT JOIN (
    SELECT 
        property_id,
        list_price / NULLIF(square_footage, 0) as price_per_sqft
    FROM listings l
    JOIN properties p ON l.property_id = p.id
    WHERE l.status = 'active'
) sqft ON p.id = sqft.property_id
WHERE zestimate IS NOT NULL
GROUP BY zip_code; 