"""
FastAPI application for housing price analysis.
Provides REST API endpoints for property search, price prediction, and market analysis.
"""

from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import os
import logging
from datetime import datetime, timedelta

# Import our modules
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.price_predictor import HousingPricePredictor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/housing_db")

# Initialize FastAPI app
app = FastAPI(
    title="Housing Price Analysis API",
    description="API for analyzing housing prices in Boulder County",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for API requests/responses
class PropertySearchRequest(BaseModel):
    min_price: Optional[int] = Field(None, description="Minimum price")
    max_price: Optional[int] = Field(None, description="Maximum price")
    min_bedrooms: Optional[int] = Field(None, description="Minimum bedrooms")
    max_bedrooms: Optional[int] = Field(None, description="Maximum bedrooms")
    min_bathrooms: Optional[float] = Field(None, description="Minimum bathrooms")
    max_bathrooms: Optional[float] = Field(None, description="Maximum bathrooms")
    min_sqft: Optional[int] = Field(None, description="Minimum square footage")
    max_sqft: Optional[int] = Field(None, description="Maximum square footage")
    cities: Optional[List[str]] = Field(None, description="Preferred cities")
    zip_codes: Optional[List[str]] = Field(None, description="Preferred zip codes")
    limit: int = Field(50, description="Maximum number of results")

class PropertyPredictionRequest(BaseModel):
    bedrooms: int = Field(..., description="Number of bedrooms")
    bathrooms: float = Field(..., description="Number of bathrooms")
    square_footage: int = Field(..., description="Square footage")
    year_built: int = Field(..., description="Year built")
    land_value: Optional[int] = Field(None, description="Land value")
    bldg_value: Optional[int] = Field(None, description="Building value")
    garage_sqft: Optional[int] = Field(None, description="Garage square footage")

class PropertyResponse(BaseModel):
    id: str
    address: str
    city: str
    zip_code: str
    bedrooms: int
    bathrooms: float
    square_footage: int
    year_built: int
    sale_price: Optional[int]
    zestimate: Optional[int]
    predicted_price: Optional[int]
    fair_price: Optional[int]
    price_difference: Optional[int]
    price_difference_percent: Optional[float]

class PredictionResponse(BaseModel):
    predicted_price: int
    confidence: float
    features_used: List[str]
    model_type: str
    fair_price: Optional[int]
    comparable_count: Optional[int]

class MarketTrendResponse(BaseModel):
    zip_code: str
    date: str
    avg_price: int
    median_price: int
    price_per_sqft: float
    inventory_count: int
    sales_count: int

class MarketSummaryResponse(BaseModel):
    total_properties: int
    avg_price: float
    median_price: float
    price_range: str
    active_listings: int
    market_trends: List[MarketTrendResponse]

# Database connection
def get_db_engine():
    """Get database engine."""
    try:
        engine = create_engine(DATABASE_URL)
        return engine
    except Exception as e:
        logger.error(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")

# ML model loading
def get_price_predictor():
    """Get the trained price prediction model."""
    try:
        model_path = "models/housing_price_model.pkl"
        if os.path.exists(model_path):
            predictor = HousingPricePredictor()
            predictor.load_model(model_path)
            return predictor
        else:
            logger.warning("Price prediction model not found")
            return None
    except Exception as e:
        logger.error(f"Error loading price predictor: {e}")
        return None

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Housing Price Analysis API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        engine = get_db_engine()
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        
        return {
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Health check failed: {e}")

@app.post("/properties/search", response_model=List[PropertyResponse])
async def search_properties(
    request: PropertySearchRequest,
    db_engine = Depends(get_db_engine)
):
    """
    Search for properties based on criteria.
    """
    try:
        # Build SQL query
        query = """
        SELECT 
            p.id,
            p.formatted_address as address,
            p.city,
            p.zip_code,
            p.bedrooms,
            p.bathrooms,
            p.square_footage,
            p.year_built,
            p.sale_price,
            p.zestimate,
            fp.fair_price,
            fp.comparable_count
        FROM properties p
        LEFT JOIN fair_prices fp ON p.id = fp.id
        WHERE 1=1
        """
        
        params = {}
        
        # Add filters
        if request.min_price:
            query += " AND (p.sale_price >= :min_price OR p.zestimate >= :min_price)"
            params['min_price'] = request.min_price
        
        if request.max_price:
            query += " AND (p.sale_price <= :max_price OR p.zestimate <= :max_price)"
            params['max_price'] = request.max_price
        
        if request.min_bedrooms:
            query += " AND p.bedrooms >= :min_bedrooms"
            params['min_bedrooms'] = request.min_bedrooms
        
        if request.max_bedrooms:
            query += " AND p.bedrooms <= :max_bedrooms"
            params['max_bedrooms'] = request.max_bedrooms
        
        if request.min_bathrooms:
            query += " AND p.bathrooms >= :min_bathrooms"
            params['min_bathrooms'] = request.min_bathrooms
        
        if request.max_bathrooms:
            query += " AND p.bathrooms <= :max_bathrooms"
            params['max_bathrooms'] = request.max_bathrooms
        
        if request.min_sqft:
            query += " AND p.square_footage >= :min_sqft"
            params['min_sqft'] = request.min_sqft
        
        if request.max_sqft:
            query += " AND p.square_footage <= :max_sqft"
            params['max_sqft'] = request.max_sqft
        
        if request.cities:
            placeholders = ','.join([f':city_{i}' for i in range(len(request.cities))])
            query += f" AND p.city IN ({placeholders})"
            for i, city in enumerate(request.cities):
                params[f'city_{i}'] = city
        
        if request.zip_codes:
            placeholders = ','.join([f':zip_{i}' for i in range(len(request.zip_codes))])
            query += f" AND p.zip_code IN ({placeholders})"
            for i, zip_code in enumerate(request.zip_codes):
                params[f'zip_{i}'] = zip_code
        
        query += " ORDER BY p.sale_price DESC NULLS LAST, p.zestimate DESC NULLS LAST"
        query += f" LIMIT {request.limit}"
        
        # Execute query
        with db_engine.connect() as conn:
            result = conn.execute(text(query), params)
            rows = result.fetchall()
        
        # Convert to response format
        properties = []
        for row in rows:
            # Calculate price difference if we have both predicted and actual
            price_difference = None
            price_difference_percent = None
            
            if row.sale_price and row.fair_price:
                price_difference = row.sale_price - row.fair_price
                price_difference_percent = (price_difference / row.fair_price) * 100
            
            property_data = {
                "id": row.id,
                "address": row.address or "Address not available",
                "city": row.city,
                "zip_code": row.zip_code,
                "bedrooms": row.bedrooms,
                "bathrooms": row.bathrooms,
                "square_footage": row.square_footage,
                "year_built": row.year_built,
                "sale_price": row.sale_price,
                "zestimate": row.zestimate,
                "predicted_price": None,  # Will be calculated if model available
                "fair_price": row.fair_price,
                "price_difference": price_difference,
                "price_difference_percent": price_difference_percent
            }
            properties.append(PropertyResponse(**property_data))
        
        return properties
        
    except Exception as e:
        logger.error(f"Error searching properties: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {e}")

@app.post("/properties/predict", response_model=PredictionResponse)
async def predict_property_price(
    request: PropertyPredictionRequest,
    predictor = Depends(get_price_predictor)
):
    """
    Predict the price of a property based on its characteristics.
    """
    try:
        if predictor is None:
            raise HTTPException(status_code=503, detail="Price prediction model not available")
        
        # Make prediction
        prediction = predictor.predict_single_property(
            bedrooms=request.bedrooms,
            bathrooms=request.bathrooms,
            square_footage=request.square_footage,
            year_built=request.year_built,
            land_value=request.land_value,
            bldg_value=request.bldg_value,
            garage_sqft=request.garage_sqft
        )
        
        # Calculate fair price (simplified - would need database lookup in production)
        fair_price = None
        comparable_count = None
        
        return PredictionResponse(
            predicted_price=prediction['predicted_price'],
            confidence=prediction['confidence'],
            features_used=prediction['features_used'],
            model_type=prediction['model_type'],
            fair_price=fair_price,
            comparable_count=comparable_count
        )
        
    except Exception as e:
        logger.error(f"Error predicting property price: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

@app.get("/market/trends", response_model=List[MarketTrendResponse])
async def get_market_trends(
    zip_code: Optional[str] = Query(None, description="Filter by zip code"),
    days: int = Query(30, description="Number of days to look back"),
    db_engine = Depends(get_db_engine)
):
    """
    Get market trends by zip code.
    """
    try:
        query = """
        SELECT 
            zip_code,
            date,
            avg_price,
            median_price,
            price_per_sqft,
            inventory_count,
            sales_count
        FROM market_trends
        WHERE date >= :start_date
        """
        
        params = {
            'start_date': datetime.now().date() - timedelta(days=days)
        }
        
        if zip_code:
            query += " AND zip_code = :zip_code"
            params['zip_code'] = zip_code
        
        query += " ORDER BY zip_code, date DESC"
        
        with db_engine.connect() as conn:
            result = conn.execute(text(query), params)
            rows = result.fetchall()
        
        trends = []
        for row in rows:
            trend = MarketTrendResponse(
                zip_code=row.zip_code,
                date=row.date.isoformat(),
                avg_price=row.avg_price,
                median_price=row.median_price,
                price_per_sqft=float(row.price_per_sqft),
                inventory_count=row.inventory_count,
                sales_count=row.sales_count
            )
            trends.append(trend)
        
        return trends
        
    except Exception as e:
        logger.error(f"Error getting market trends: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get market trends: {e}")

@app.get("/market/summary", response_model=MarketSummaryResponse)
async def get_market_summary(
    db_engine = Depends(get_db_engine)
):
    """
    Get overall market summary.
    """
    try:
        # Get market summary from view
        query = """
        SELECT 
            COUNT(*) as total_properties,
            AVG(zestimate) as avg_price,
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY zestimate) as median_price,
            MIN(zestimate) as min_price,
            MAX(zestimate) as max_price,
            COUNT(CASE WHEN status = 'active' THEN 1 END) as active_listings
        FROM properties
        WHERE zestimate IS NOT NULL
        """
        
        with db_engine.connect() as conn:
            result = conn.execute(text(query))
            row = result.fetchone()
        
        if row:
            summary = MarketSummaryResponse(
                total_properties=row.total_properties,
                avg_price=float(row.avg_price) if row.avg_price else 0,
                median_price=float(row.median_price) if row.median_price else 0,
                price_range=f"${row.min_price:,} - ${row.max_price:,}" if row.min_price and row.max_price else "N/A",
                active_listings=row.active_listings,
                market_trends=[]  # Would need to fetch recent trends
            )
            return summary
        else:
            raise HTTPException(status_code=404, detail="No market data available")
        
    except Exception as e:
        logger.error(f"Error getting market summary: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get market summary: {e}")

@app.get("/properties/{property_id}", response_model=PropertyResponse)
async def get_property_details(
    property_id: str,
    db_engine = Depends(get_db_engine)
):
    """
    Get detailed information about a specific property.
    """
    try:
        query = """
        SELECT 
            p.id,
            p.formatted_address as address,
            p.city,
            p.zip_code,
            p.bedrooms,
            p.bathrooms,
            p.square_footage,
            p.year_built,
            p.sale_price,
            p.zestimate,
            fp.fair_price,
            fp.comparable_count
        FROM properties p
        LEFT JOIN fair_prices fp ON p.id = fp.id
        WHERE p.id = :property_id
        """
        
        with db_engine.connect() as conn:
            result = conn.execute(text(query), {"property_id": property_id})
            row = result.fetchone()
        
        if not row:
            raise HTTPException(status_code=404, detail="Property not found")
        
        # Calculate price difference
        price_difference = None
        price_difference_percent = None
        
        if row.sale_price and row.fair_price:
            price_difference = row.sale_price - row.fair_price
            price_difference_percent = (price_difference / row.fair_price) * 100
        
        property_data = {
            "id": row.id,
            "address": row.address or "Address not available",
            "city": row.city,
            "zip_code": row.zip_code,
            "bedrooms": row.bedrooms,
            "bathrooms": row.bathrooms,
            "square_footage": row.square_footage,
            "year_built": row.year_built,
            "sale_price": row.sale_price,
            "zestimate": row.zestimate,
            "predicted_price": None,
            "fair_price": row.fair_price,
            "price_difference": price_difference,
            "price_difference_percent": price_difference_percent
        }
        
        return PropertyResponse(**property_data)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting property details: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get property details: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 