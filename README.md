# Housing Price Analysis App

A data-driven housing market analysis platform for Boulder County, Colorado, designed to help users understand property pricing drivers and make informed real estate decisions.

## 🎯 Project Overview

This app combines multiple data sources to provide:
- **ML-powered price predictions** based on property characteristics
- **Market trend analysis** using real-time and historical data
- **Realtor performance evaluation** using transaction history
- **User preference matching** for personalized property recommendations

## 📊 Data Sources

### 1. RentCast API (Real-time)
- **Property Data**: Detailed property characteristics (beds, baths, sqft, year built, etc.)
- **Property Listings**: Active sale/rental listings with pricing and agent info
- **Property Valuations**: Automated valuation model (AVM) estimates
- **Market Data**: Aggregated market statistics by zip code

### 2. Boulder County Transaction Data (Monthly)
- **Sales History**: Complete transaction records with property details
- **Realtor Information**: Agent names and transaction performance
- **Property Characteristics**: Detailed building and lot information

### 3. Zillow Static Data (Monthly)
- **Market Trends**: Inventory, pricing, and days on market statistics
- **Historical Data**: Long-term market performance metrics

## 🗄️ Database Schema

The database is designed with the following key tables:

### Core Tables
- `properties` - Property characteristics from RentCast
- `property_listings` - Active listings with pricing and agent info
- `property_valuations` - AVM estimates and confidence scores

### Transaction Data
- `boulder_transactions` - Historical sales from Boulder County
- `realtors` - Realtor information and contact details
- `realtor_performance` - Transaction performance metrics

### Market Data
- `market_trends` - Aggregated market statistics by zip code
- `market_data_by_type` - Statistics broken down by property type
- `market_data_by_bedrooms` - Statistics broken down by bedroom count

### User Data
- `user_preferences` - User search criteria and preferences
- `user_saved_properties` - User-saved properties with notes and ratings

### ML Model Data
- `model_predictions` - ML model price predictions and confidence scores
- `model_performance` - Model evaluation metrics (RMSE, MAE, R²)

## 🏗️ Project Structure

```
housing-app/
├── data/                    # Raw and processed datasets
│   ├── raw/                # Original data files
│   └── processed/          # Cleaned and transformed data
├── notebooks/              # Jupyter notebooks for EDA and prototyping
├── src/                    # Source code
│   ├── data/              # Data loading, cleaning, feature engineering
│   ├── models/            # ML model training and evaluation
│   ├── analysis/          # EDA, feature importance, interpretability
│   └── api/               # FastAPI/Flask API for serving models
├── tests/                 # Unit and integration tests
├── database_schema.sql    # PostgreSQL schema definition
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Railway/Render account (for database hosting)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kaiasdad01/real-estate-pricing.git
   cd real-estate-pricing
   ```

2. **Set up PostgreSQL database**
   - Create a new PostgreSQL database on Railway/Render
   - Run the schema: `psql -d your_database -f database_schema.sql`

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   export RENTCAST_API_KEY=your_api_key
   export DATABASE_URL=your_postgresql_url
   ```

## 📈 Key Features

### 1. Fair Price Calculation
- **Comparable Properties**: Find similar properties based on beds, baths, sqft, location
- **Median Price Analysis**: Calculate fair price as median of comparable properties
- **Market Adjustment**: Adjust for current market conditions

### 2. ML Price Prediction
- **Feature Engineering**: Create features from property characteristics
- **Model Training**: Train regression models (XGBoost, Random Forest)
- **Prediction Confidence**: Provide confidence intervals for predictions
- **Feature Importance**: Explain what drives pricing in the area

### 3. Realtor Performance Analysis
- **Transaction Volume**: Count transactions in specific price ranges
- **Sale-to-List Ratio**: Analyze negotiation effectiveness
- **Geographic Expertise**: Identify realtors with experience in target areas
- **ADU Experience**: Find realtors with ADU transaction history

### 4. Market Analytics
- **Inventory Trends**: Track available inventory over time
- **Price Trends**: Monitor median and average price changes
- **Days on Market**: Analyze market velocity
- **Seasonal Patterns**: Identify best times to buy/sell

## 🔄 Data Pipeline

### Daily Updates (RentCast API)
- Property listings and valuations
- Market data by zip code
- New property data

### Monthly Updates (Static Data)
- Boulder County transaction data (5th of month)
- Zillow market trends (16th of month)

### ML Model Updates
- Retrain models with new transaction data
- Update feature importance analysis
- Recalculate performance metrics

## 🎯 Next Steps

### Phase 1: Data Foundation (Week 1-2)
- [ ] Set up PostgreSQL on Railway/Render
- [ ] Create Dagster pipeline for data ingestion
- [ ] Load Boulder County transaction data
- [ ] Set up RentCast API integration

### Phase 2: Feature Engineering & EDA (Week 3-4)
- [ ] Analyze Boulder County data for pricing drivers
- [ ] Create feature engineering pipeline
- [ ] Build EDA notebooks for market insights
- [ ] Define "similar properties" logic

### Phase 3: Model Development (Week 5-6)
- [ ] Build ML training pipeline with Dagster
- [ ] Implement fair price calculation
- [ ] Create over/under pricing scoring
- [ ] Develop feature importance analysis

### Phase 4: Realtor Analytics (Week 7-8)
- [ ] Build realtor performance metrics
- [ ] Create realtor scoring system
- [ ] Develop realtor recommendation engine

### Phase 5: Web Application (Week 9-12)
- [ ] Build FastAPI backend
- [ ] Create React frontend
- [ ] Implement user authentication
- [ ] Deploy to production

## 📊 Key Metrics

### Model Performance Targets
- **RMSE**: < 10% of median home price
- **MAE**: < 8% of median home price
- **R²**: > 0.85

### Business Metrics
- **Fair Price Accuracy**: 90% within 5% of actual sale price
- **Realtor Recommendations**: Top 3 realtors have >80% success rate
- **User Engagement**: >70% of users save at least 3 properties

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- **Project Link**: [https://github.com/kaiasdad01/real-estate-pricing](https://github.com/kaiasdad01/real-estate-pricing)
- **Issues**: [https://github.com/kaiasdad01/real-estate-pricing/issues](https://github.com/kaiasdad01/real-estate-pricing/issues)

---

**Note**: This project is designed for educational and portfolio purposes. Always verify data accuracy and consult with real estate professionals for actual investment decisions.
