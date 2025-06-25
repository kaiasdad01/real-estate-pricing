"""
Dagster assets for housing price analysis data pipeline.
Handles data loading, processing, and ML model training.
"""

import pandas as pd
import numpy as np
from dagster import asset, AssetExecutionContext, MetadataValue
from sqlalchemy import create_engine, text
import requests
import json
from datetime import datetime, timedelta
import os
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/housing_db")

# RentCast API configuration
RENTCAST_API_KEY = os.getenv("RENTCAST_API_KEY")
RENTCAST_BASE_URL = "https://api.rentcast.io/v1"

@asset
def boulder_county_transactions(context: AssetExecutionContext) -> pd.DataFrame:
    """
    Load Boulder County transaction data from CSV file.
    """
    try:
        # Load the CSV file
        df = pd.read_csv("boco-sales.csv")
        
        # Clean and standardize column names
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        
        # Convert sale price to integer (remove $ and commas)
        df['sale_price'] = df['sale_price'].str.replace('$', '').str.replace(',', '').astype(int)
        
        # Convert sale date to datetime
        df['sale_date'] = pd.to_datetime(df['sale_date'], format='%m/%d/%Y')
        
        # Filter for recent transactions (last 5 years)
        five_years_ago = datetime.now() - timedelta(days=5*365)
        df = df[df['sale_date'] >= five_years_ago]
        
        # Add metadata
        context.add_output_metadata({
            "num_records": MetadataValue.int(len(df)),
            "date_range": MetadataValue.text(f"{df['sale_date'].min()} to {df['sale_date'].max()}"),
            "total_sales_volume": MetadataValue.int(df['sale_price'].sum()),
            "avg_sale_price": MetadataValue.int(df['sale_price'].mean())
        })
        
        logger.info(f"Loaded {len(df)} Boulder County transactions")
        return df
        
    except Exception as e:
        logger.error(f"Error loading Boulder County data: {e}")
        raise

@asset
def rentcast_properties(context: AssetExecutionContext) -> pd.DataFrame:
    """
    Load property data from RentCast API.
    Limited to 50 requests per month as per API limits.
    """
    if not RENTCAST_API_KEY:
        logger.warning("RENTCAST_API_KEY not found, skipping RentCast data load")
        return pd.DataFrame()
    
    try:
        # For MVP, we'll focus on Boulder County zip codes
        boulder_zip_codes = [
            "80301", "80302", "80303", "80304", "80305",  # Boulder
            "80026", "80027",  # Lafayette, Louisville
            "80516",  # Erie
            "80501", "80503", "80504",  # Longmont
            "80027"   # Superior
        ]
        
        all_properties = []
        
        for zip_code in boulder_zip_codes[:5]:  # Limit to 5 zip codes to stay within API limits
            url = f"{RENTCAST_BASE_URL}/properties"
            params = {
                "zipCode": zip_code,
                "propertyType": "SingleFamily",
                "status": "Active",
                "limit": 10  # Limit per zip code
            }
            headers = {"X-Api-Key": RENTCAST_API_KEY}
            
            response = requests.get(url, params=params, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                properties = data.get("properties", [])
                all_properties.extend(properties)
                logger.info(f"Loaded {len(properties)} properties for zip code {zip_code}")
            else:
                logger.warning(f"Failed to load data for zip code {zip_code}: {response.status_code}")
        
        if all_properties:
            df = pd.DataFrame(all_properties)
            
            # Add metadata
            context.add_output_metadata({
                "num_properties": MetadataValue.int(len(df)),
                "zip_codes_covered": MetadataValue.text(", ".join(boulder_zip_codes[:5])),
                "avg_price": MetadataValue.int(df.get('zestimate', pd.Series()).mean())
            })
            
            logger.info(f"Loaded {len(df)} properties from RentCast")
            return df
        else:
            logger.warning("No properties loaded from RentCast")
            return pd.DataFrame()
            
    except Exception as e:
        logger.error(f"Error loading RentCast data: {e}")
        return pd.DataFrame()

@asset
def processed_properties(
    context: AssetExecutionContext,
    boulder_county_transactions: pd.DataFrame,
    rentcast_properties: pd.DataFrame
) -> pd.DataFrame:
    """
    Process and combine property data from multiple sources.
    """
    try:
        # Process Boulder County transactions
        boulder_df = boulder_county_transactions.copy()
        
        # Create property records from transactions
        boulder_properties = boulder_df[[
            'parcel_nb', 'property_address', 'city', 'sale_date', 'sale_price',
            'bedrooms', 'full_baths', 'three_qtr_baths', 'half_baths',
            'above_ground_sqft', 'finished_bsmt_sqft', 'unfinished_bsmt_sqft',
            'garage_sqft', 'year_built', 'land_value', 'bldg_value'
        ]].copy()
        
        # Calculate total bathrooms
        boulder_properties['bathrooms'] = (
            boulder_properties['full_baths'] + 
            boulder_properties['three_qtr_baths'] * 0.75 + 
            boulder_properties['half_baths'] * 0.5
        )
        
        # Calculate total square footage
        boulder_properties['square_footage'] = (
            boulder_properties['above_ground_sqft'] + 
            boulder_properties['finished_bsmt_sqft']
        )
        
        # Add source identifier
        boulder_properties['data_source'] = 'boulder_county'
        boulder_properties['id'] = boulder_properties['parcel_nb']
        
        # Process RentCast properties if available
        if not rentcast_properties.empty:
            rentcast_df = rentcast_properties.copy()
            rentcast_df['data_source'] = 'rentcast'
            
            # Standardize column names
            column_mapping = {
                'id': 'id',
                'formattedAddress': 'formatted_address',
                'addressLine1': 'address_line1',
                'city': 'city',
                'state': 'state',
                'zipCode': 'zip_code',
                'bedrooms': 'bedrooms',
                'bathrooms': 'bathrooms',
                'squareFootage': 'square_footage',
                'yearBuilt': 'year_built',
                'zestimate': 'zestimate',
                'lastSalePrice': 'last_sale_price',
                'lastSaleDate': 'last_sale_date'
            }
            
            rentcast_df = rentcast_df.rename(columns=column_mapping)
            
            # Combine datasets
            combined_df = pd.concat([boulder_properties, rentcast_df], ignore_index=True)
        else:
            combined_df = boulder_properties
        
        # Clean and validate data
        combined_df = combined_df.dropna(subset=['sale_price', 'bedrooms', 'bathrooms'])
        
        # Remove outliers (properties with extreme prices)
        price_q1 = combined_df['sale_price'].quantile(0.25)
        price_q3 = combined_df['sale_price'].quantile(0.75)
        price_iqr = price_q3 - price_q1
        price_lower = price_q1 - 1.5 * price_iqr
        price_upper = price_q3 + 1.5 * price_iqr
        
        combined_df = combined_df[
            (combined_df['sale_price'] >= price_lower) & 
            (combined_df['sale_price'] <= price_upper)
        ]
        
        # Add metadata
        context.add_output_metadata({
            "total_properties": MetadataValue.int(len(combined_df)),
            "boulder_county_properties": MetadataValue.int(len(boulder_properties)),
            "rentcast_properties": MetadataValue.int(len(rentcast_properties)),
            "price_range": MetadataValue.text(f"${combined_df['sale_price'].min():,} - ${combined_df['sale_price'].max():,}"),
            "avg_price": MetadataValue.int(combined_df['sale_price'].mean())
        })
        
        logger.info(f"Processed {len(combined_df)} total properties")
        return combined_df
        
    except Exception as e:
        logger.error(f"Error processing properties: {e}")
        raise

@asset
def market_trends(
    context: AssetExecutionContext,
    processed_properties: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate market trends by zip code.
    """
    try:
        if processed_properties.empty:
            logger.warning("No properties to calculate market trends")
            return pd.DataFrame()
        
        # Group by zip code and calculate trends
        trends = []
        
        for zip_code in processed_properties['zip_code'].unique():
            if pd.isna(zip_code):
                continue
                
            zip_data = processed_properties[processed_properties['zip_code'] == zip_code]
            
            if len(zip_data) < 5:  # Need minimum data points
                continue
            
            trend = {
                'zip_code': zip_code,
                'date': datetime.now().date(),
                'data_source': 'combined',
                'avg_price': int(zip_data['sale_price'].mean()),
                'median_price': int(zip_data['sale_price'].median()),
                'price_per_sqft': float(zip_data['sale_price'].sum() / zip_data['square_footage'].sum()),
                'inventory_count': len(zip_data),
                'sales_count': len(zip_data)
            }
            trends.append(trend)
        
        trends_df = pd.DataFrame(trends)
        
        # Add metadata
        context.add_output_metadata({
            "num_zip_codes": MetadataValue.int(len(trends_df)),
            "zip_codes": MetadataValue.text(", ".join(trends_df['zip_code'].astype(str))),
            "avg_market_price": MetadataValue.int(trends_df['avg_price'].mean())
        })
        
        logger.info(f"Calculated market trends for {len(trends_df)} zip codes")
        return trends_df
        
    except Exception as e:
        logger.error(f"Error calculating market trends: {e}")
        return pd.DataFrame()

@asset
def ml_training_data(
    context: AssetExecutionContext,
    processed_properties: pd.DataFrame
) -> pd.DataFrame:
    """
    Prepare data for ML model training.
    """
    try:
        if processed_properties.empty:
            logger.warning("No properties to prepare for ML training")
            return pd.DataFrame()
        
        # Select features for ML model
        features = [
            'bedrooms', 'bathrooms', 'square_footage', 'year_built',
            'land_value', 'bldg_value', 'garage_sqft'
        ]
        
        # Create feature matrix
        X = processed_properties[features].copy()
        y = processed_properties['sale_price']
        
        # Handle missing values
        X = X.fillna(X.median())
        
        # Remove rows with missing target
        mask = ~y.isna()
        X = X[mask]
        y = y[mask]
        
        # Add engineered features
        X['price_per_sqft'] = y / X['square_footage']
        X['total_bathrooms'] = X['bathrooms']
        X['age'] = datetime.now().year - X['year_built']
        X['land_to_building_ratio'] = X['land_value'] / (X['bldg_value'] + 1)
        
        # Combine features and target
        training_data = X.copy()
        training_data['sale_price'] = y
        
        # Add metadata
        context.add_output_metadata({
            "training_samples": MetadataValue.int(len(training_data)),
            "features": MetadataValue.text(", ".join(X.columns)),
            "target_range": MetadataValue.text(f"${y.min():,} - ${y.max():,}"),
            "avg_target": MetadataValue.int(y.mean())
        })
        
        logger.info(f"Prepared {len(training_data)} samples for ML training")
        return training_data
        
    except Exception as e:
        logger.error(f"Error preparing ML training data: {e}")
        return pd.DataFrame()

@asset
def database_connection() -> Dict:
    """
    Create database connection for storing processed data.
    """
    try:
        engine = create_engine(DATABASE_URL)
        
        # Test connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        
        logger.info("Database connection established")
        return {"engine": engine, "url": DATABASE_URL}
        
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        raise

@asset
def load_to_database(
    context: AssetExecutionContext,
    processed_properties: pd.DataFrame,
    market_trends: pd.DataFrame,
    database_connection: Dict
) -> None:
    """
    Load processed data to PostgreSQL database.
    """
    try:
        engine = database_connection["engine"]
        
        # Load properties
        if not processed_properties.empty:
            processed_properties.to_sql(
                'properties', 
                engine, 
                if_exists='append', 
                index=False,
                method='multi'
            )
            logger.info(f"Loaded {len(processed_properties)} properties to database")
        
        # Load market trends
        if not market_trends.empty:
            market_trends.to_sql(
                'market_trends', 
                engine, 
                if_exists='append', 
                index=False,
                method='multi'
            )
            logger.info(f"Loaded {len(market_trends)} market trends to database")
        
        # Add metadata
        context.add_output_metadata({
            "properties_loaded": MetadataValue.int(len(processed_properties)),
            "trends_loaded": MetadataValue.int(len(market_trends)),
            "database_url": MetadataValue.text(database_connection["url"])
        })
        
    except Exception as e:
        logger.error(f"Error loading data to database: {e}")
        raise 