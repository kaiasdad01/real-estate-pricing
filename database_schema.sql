-- Database Schema for Housing Price Analysis App
-- PostgreSQL schema for Boulder County housing market analysis

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
    bedrooms INTEGER,
    bathrooms DECIMAL(4, 1),
    square_footage INTEGER,
    lot_size INTEGER,
    year_built INTEGER,
    assessor_id VARCHAR(100),
    legal_description TEXT,
    subdivision VARCHAR(255),
    zoning VARCHAR(50),
    last_sale_date DATE,
    last_sale_price INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Property listings (from rentcast.io listings)
CREATE TABLE property_listings (
    id SERIAL PRIMARY KEY,
    property_id VARCHAR(255) REFERENCES properties(id),
    listing_type VARCHAR(20), -- 'sale' or 'rental'
    list_price INTEGER,
    list_date DATE,
    days_on_market INTEGER,
    status VARCHAR(50), -- 'active', 'pending', 'sold', 'withdrawn'
    mls_number VARCHAR(100),
    listing_agent_name VARCHAR(255),
    listing_agent_phone VARCHAR(50),
    listing_agent_email VARCHAR(255),
    listing_office_name VARCHAR(255),
    listing_office_phone VARCHAR(50),
    listing_office_email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Property valuations (from rentcast.io AVM)
CREATE TABLE property_valuations (
    id SERIAL PRIMARY KEY,
    property_id VARCHAR(255) REFERENCES properties(id),
    valuation_date DATE,
    estimated_value INTEGER,
    value_range_low INTEGER,
    value_range_high INTEGER,
    confidence_score DECIMAL(3, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- BOULDER COUNTY TRANSACTION DATA
-- =====================================================

-- Boulder County sales transactions
CREATE TABLE boulder_transactions (
    id SERIAL PRIMARY KEY,
    market_area VARCHAR(10),
    account_no VARCHAR(50),
    parcel_nb VARCHAR(50),
    property_address TEXT,
    loc_city VARCHAR(100),
    subname VARCHAR(255),
    multiple_bldgs VARCHAR(10),
    account_type VARCHAR(50),
    bldg1_description VARCHAR(255),
    bldg1_design VARCHAR(100),
    bldg1_year_built INTEGER,
    bedrooms INTEGER,
    full_baths INTEGER,
    three_qtr_baths INTEGER,
    half_baths INTEGER,
    above_ground_sqft INTEGER,
    finished_bsmt_sqft INTEGER,
    unfinished_bsmt_sqft INTEGER,
    garage_sqft INTEGER,
    finished_garage_sqft INTEGER,
    studio_sqft INTEGER,
    other_bldgs INTEGER,
    reception_no INTEGER,
    sale_date DATE,
    sale_price INTEGER,
    grantor TEXT,
    grantee TEXT,
    owner_name TEXT,
    care_of TEXT,
    mailing_addr1 TEXT,
    mailing_addr2 TEXT,
    city VARCHAR(100),
    state VARCHAR(2),
    zipcode VARCHAR(10),
    land_value INTEGER,
    bldg_value INTEGER,
    extra_feature_value INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- MARKET DATA (from rentcast.io and Zillow)
-- =====================================================

-- Market trends (aggregated by zip code)
CREATE TABLE market_trends (
    id SERIAL PRIMARY KEY,
    zip_code VARCHAR(10),
    date DATE,
    data_source VARCHAR(50), -- 'rentcast' or 'zillow'
    
    -- Sale data
    avg_price INTEGER,
    median_price INTEGER,
    min_price INTEGER,
    max_price INTEGER,
    avg_price_per_sqft DECIMAL(10, 2),
    median_price_per_sqft DECIMAL(10, 2),
    avg_sqft INTEGER,
    median_sqft INTEGER,
    avg_days_on_market INTEGER,
    median_days_on_market INTEGER,
    new_listings INTEGER,
    total_listings INTEGER,
    
    -- Inventory data
    available_inventory INTEGER,
    pending_inventory INTEGER,
    sold_inventory INTEGER,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(zip_code, date, data_source)
);

-- Market data by property type
CREATE TABLE market_data_by_type (
    id SERIAL PRIMARY KEY,
    market_trend_id INTEGER REFERENCES market_trends(id),
    property_type VARCHAR(50),
    avg_price INTEGER,
    median_price INTEGER,
    min_price INTEGER,
    max_price INTEGER,
    avg_price_per_sqft DECIMAL(10, 2),
    median_price_per_sqft DECIMAL(10, 2),
    avg_sqft INTEGER,
    median_sqft INTEGER,
    avg_days_on_market INTEGER,
    median_days_on_market INTEGER,
    new_listings INTEGER,
    total_listings INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Market data by bedrooms
CREATE TABLE market_data_by_bedrooms (
    id SERIAL PRIMARY KEY,
    market_trend_id INTEGER REFERENCES market_trends(id),
    bedrooms INTEGER,
    avg_price INTEGER,
    median_price INTEGER,
    min_price INTEGER,
    max_price INTEGER,
    avg_price_per_sqft DECIMAL(10, 2),
    median_price_per_sqft DECIMAL(10, 2),
    avg_sqft INTEGER,
    median_sqft INTEGER,
    avg_days_on_market INTEGER,
    median_days_on_market INTEGER,
    new_listings INTEGER,
    total_listings INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- REALTOR PERFORMANCE DATA
-- =====================================================

-- Realtor information
CREATE TABLE realtors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(50),
    email VARCHAR(255),
    office_name VARCHAR(255),
    license_number VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Realtor transaction performance
CREATE TABLE realtor_performance (
    id SERIAL PRIMARY KEY,
    realtor_id INTEGER REFERENCES realtors(id),
    transaction_id INTEGER REFERENCES boulder_transactions(id),
    role VARCHAR(50), -- 'listing_agent', 'buying_agent'
    sale_price INTEGER,
    list_price INTEGER,
    days_on_market INTEGER,
    sale_date DATE,
    property_type VARCHAR(50),
    bedrooms INTEGER,
    bathrooms DECIMAL(4, 1),
    square_footage INTEGER,
    zip_code VARCHAR(10),
    has_adu BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- USER DATA
-- =====================================================

-- User preferences
CREATE TABLE user_preferences (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255), -- Will be linked to auth system
    min_price INTEGER,
    max_price INTEGER,
    min_bedrooms INTEGER,
    max_bedrooms INTEGER,
    min_bathrooms DECIMAL(4, 1),
    max_bathrooms DECIMAL(4, 1),
    min_sqft INTEGER,
    max_sqft INTEGER,
    property_types TEXT[], -- Array of property types
    zip_codes TEXT[], -- Array of zip codes
    must_have_features TEXT[], -- ['garage', 'adu', 'basement']
    preferred_features TEXT[], -- ['yard', 'mountain_view']
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User saved properties
CREATE TABLE user_saved_properties (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255),
    property_id VARCHAR(255) REFERENCES properties(id),
    status VARCHAR(50), -- 'interested', 'toured', 'not_interested', 'offered'
    notes TEXT,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- ML MODEL DATA
-- =====================================================

-- Model predictions
CREATE TABLE model_predictions (
    id SERIAL PRIMARY KEY,
    property_id VARCHAR(255) REFERENCES properties(id),
    model_version VARCHAR(50),
    predicted_price INTEGER,
    confidence_score DECIMAL(3, 2),
    feature_importance JSONB, -- Store SHAP values or feature importance
    prediction_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Model performance metrics
CREATE TABLE model_performance (
    id SERIAL PRIMARY KEY,
    model_version VARCHAR(50),
    metric_name VARCHAR(100), -- 'rmse', 'mae', 'r2'
    metric_value DECIMAL(10, 4),
    evaluation_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- INDEXES FOR PERFORMANCE
-- =====================================================

-- Properties indexes
CREATE INDEX idx_properties_zip_code ON properties(zip_code);
CREATE INDEX idx_properties_city ON properties(city);
CREATE INDEX idx_properties_property_type ON properties(property_type);
CREATE INDEX idx_properties_bedrooms ON properties(bedrooms);
CREATE INDEX idx_properties_price_range ON properties(last_sale_price);

-- Listings indexes
CREATE INDEX idx_listings_property_id ON property_listings(property_id);
CREATE INDEX idx_listings_status ON property_listings(status);
CREATE INDEX idx_listings_date ON property_listings(list_date);

-- Boulder transactions indexes
CREATE INDEX idx_boulder_transactions_sale_date ON boulder_transactions(sale_date);
CREATE INDEX idx_boulder_transactions_sale_price ON boulder_transactions(sale_price);
CREATE INDEX idx_boulder_transactions_zipcode ON boulder_transactions(zipcode);

-- Market trends indexes
CREATE INDEX idx_market_trends_zip_date ON market_trends(zip_code, date);
CREATE INDEX idx_market_trends_source ON market_trends(data_source);

-- Realtor performance indexes
CREATE INDEX idx_realtor_performance_realtor_id ON realtor_performance(realtor_id);
CREATE INDEX idx_realtor_performance_sale_date ON realtor_performance(sale_date);

-- User data indexes
CREATE INDEX idx_user_preferences_user_id ON user_preferences(user_id);
CREATE INDEX idx_user_saved_properties_user_id ON user_saved_properties(user_id);

-- Model data indexes
CREATE INDEX idx_model_predictions_property_id ON model_predictions(property_id);
CREATE INDEX idx_model_predictions_date ON model_predictions(prediction_date);

-- =====================================================
-- TRIGGERS FOR UPDATED_AT
-- =====================================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply triggers to tables with updated_at
CREATE TRIGGER update_properties_updated_at BEFORE UPDATE ON properties FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_listings_updated_at BEFORE UPDATE ON property_listings FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_user_preferences_updated_at BEFORE UPDATE ON user_preferences FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_user_saved_properties_updated_at BEFORE UPDATE ON user_saved_properties FOR EACH ROW EXECUTE FUNCTION update_updated_at_column(); 