# Housing Price Analysis App - Revised Implementation

## 🎯 Project Overview

A data-driven housing market analysis platform for Boulder County, Colorado, designed to help users understand property pricing drivers and make informed real estate decisions.

**⚠️ IMPORTANT: This implementation focuses ONLY on what we can actually build with the available data sources.**

## ✅ What We CAN Build

### 1. **Property Pricing Model**
- ML model to predict prices based on property characteristics
- Uses Random Forest, Gradient Boosting, or Linear Regression
- Features: bedrooms, bathrooms, square footage, year built, land value, building value, garage space

### 2. **Fair Price Calculator**
- Median price of comparable properties (similar beds/baths/sqft/location)
- Helps users understand market value vs. list price

### 3. **Market Trend Analysis**
- Zip code level trends over time
- Price per square foot analysis
- Inventory and sales volume tracking

### 4. **Property Search & Matching**
- Search properties by criteria (price, beds, baths, location)
- User preference matching
- Property comparison tools

### 5. **Over/Under Pricing Detection**
- Compare list price to predicted price
- Identify potentially overpriced or underpriced properties

## ❌ What We CANNOT Build

### **Realtor Performance Analysis**
- ❌ Agent transaction history
- ❌ Realtor performance metrics
- ❌ Agent recommendations
- ❌ Agent matching

**Why?** Boulder County data only provides buyer/seller names (grantor/grantee), not agent information. RentCast only provides agent data for active listings, not historical sales.

## 📊 Data Sources

### 1. **Boulder County Transaction Data** (`boco-sales.csv`)
- **What it provides**: Historical sales transactions with buyer/seller names
- **What it lacks**: Agent information, current listings
- **Use case**: Training ML models, market trend analysis

### 2. **RentCast API** (50 requests/month limit)
- **What it provides**: Current property data, active listings, agent info for current listings
- **What it lacks**: Historical agent data, comprehensive historical sales
- **Use case**: Current market data, property characteristics

### 3. **Zillow Data** (Static monthly files)
- **What it provides**: Market trends, price indices
- **What it lacks**: Individual property data, agent information
- **Use case**: Market trend analysis, price indices

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Sources  │    │   Dagster       │    │   PostgreSQL    │
│                 │    │   Pipeline      │    │   Database      │
│ • Boulder CSV   │───▶│ • Data Loading  │───▶│ • Properties    │
│ • RentCast API  │    │ • Processing    │    │ • Transactions  │
│ • Zillow Data   │    │ • ML Training   │    │ • Market Trends │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   FastAPI       │
                       │   Application   │
                       │ • Property API  │
                       │ • Price Predict │
                       │ • Market Trends │
                       └─────────────────┘
```

## 📁 Project Structure

```
housing-app/
├── data/
│   ├── raw/                    # Raw data files
│   └── processed/              # Processed data
├── src/
│   ├── data/
│   │   └── dagster_assets.py   # Data pipeline orchestration
│   ├── models/
│   │   └── price_predictor.py  # ML model for price prediction
│   ├── analysis/               # Data analysis scripts
│   └── api/
│       └── main.py             # FastAPI application
├── notebooks/                  # Jupyter notebooks for EDA
├── tests/                      # Unit tests
├── database_schema_revised.sql # Database schema (no realtor tables)
├── requirements.txt            # Python dependencies
└── README_REVISED.md          # This file
```

## 🚀 Quick Start

### 1. **Environment Setup**

```bash
# Clone the repository
git clone https://github.com/kaiasdad01/real-estate-pricing.git
cd real-estate-pricing

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. **Database Setup**

```bash
# Set up PostgreSQL database (using Railway/Render)
# Create database and get connection string

# Set environment variables
export DATABASE_URL="postgresql://user:password@host:port/database"
export RENTCAST_API_KEY="your_api_key_here"
```

### 3. **Database Schema**

```bash
# Create database tables
psql $DATABASE_URL -f database_schema_revised.sql
```

### 4. **Data Pipeline**

```bash
# Run Dagster pipeline to load and process data
dagster dev
```

### 5. **Train ML Model**

```python
# In Python notebook or script
from src.models.price_predictor import train_price_model
import pandas as pd

# Load processed data
data = pd.read_csv("data/processed/properties.csv")

# Train model
predictor = train_price_model(data, model_type='random_forest', save_path='models/housing_price_model.pkl')
```

### 6. **Start API Server**

```bash
# Start FastAPI application
cd src/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📋 API Endpoints

### Property Search
```http
POST /properties/search
{
  "min_price": 500000,
  "max_price": 1000000,
  "min_bedrooms": 3,
  "max_bedrooms": 5,
  "cities": ["Boulder", "Louisville"],
  "limit": 50
}
```

### Price Prediction
```http
POST /properties/predict
{
  "bedrooms": 3,
  "bathrooms": 2.5,
  "square_footage": 2000,
  "year_built": 1995,
  "land_value": 300000,
  "bldg_value": 400000
}
```

### Market Trends
```http
GET /market/trends?zip_code=80301&days=30
```

### Market Summary
```http
GET /market/summary
```

## 🔧 Configuration

### Environment Variables

```bash
# Database
DATABASE_URL=postgresql://user:password@host:port/database

# RentCast API (optional - limited to 50 requests/month)
RENTCAST_API_KEY=your_api_key_here

# Model settings
MODEL_TYPE=random_forest  # or gradient_boosting, linear
MODEL_SAVE_PATH=models/housing_price_model.pkl
```

### Dagster Configuration

The data pipeline is configured in `src/data/dagster_assets.py`:
- Boulder County data loading
- RentCast API integration (with rate limiting)
- Data processing and cleaning
- ML training data preparation
- Database loading

## 📈 ML Model Details

### Features Used
- **Basic**: bedrooms, bathrooms, square footage, year built
- **Financial**: land value, building value, garage square footage
- **Engineered**: price per sqft, property age, land-to-building ratio

### Model Types
1. **Random Forest** (default) - Good for non-linear relationships
2. **Gradient Boosting** - High accuracy, slower training
3. **Linear Regression** - Fast, interpretable, linear relationships only

### Model Performance
- **R² Score**: Measures prediction accuracy
- **RMSE**: Root mean square error in dollars
- **MAE**: Mean absolute error in dollars
- **MAPE**: Mean absolute percentage error

## 🧪 Testing

```bash
# Run tests
pytest tests/

# Run specific test
pytest tests/test_price_predictor.py
```

## 📊 Data Limitations & Considerations

### Boulder County Data
- **Strengths**: Comprehensive historical transactions, detailed property characteristics
- **Limitations**: No agent information, no current listings
- **Update frequency**: Static (monthly/quarterly)

### RentCast API
- **Strengths**: Current property data, active listings, agent info for current listings
- **Limitations**: 50 requests/month limit, no historical agent data
- **Update frequency**: Real-time (with API limits)

### Zillow Data
- **Strengths**: Market trends, price indices, multiple geographic levels
- **Limitations**: No individual property data, no agent information
- **Update frequency**: Monthly

## 🚀 Deployment

### Production Setup

1. **Database**: Use PostgreSQL on Railway/Render
2. **API**: Deploy FastAPI on Railway/Render
3. **Pipeline**: Schedule Dagster jobs for regular data updates
4. **Monitoring**: Add logging and error tracking

### Scaling Considerations

- **API Rate Limiting**: Implement for RentCast API
- **Database Indexing**: Optimize for property searches
- **Caching**: Cache market trends and predictions
- **Load Balancing**: For high-traffic scenarios

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

For questions or issues:
1. Check the documentation
2. Review the data limitations section
3. Open an issue on GitHub

---

**Note**: This implementation is honest about its limitations. We cannot provide realtor performance analysis due to data constraints, but we can provide valuable property pricing insights and market analysis. 