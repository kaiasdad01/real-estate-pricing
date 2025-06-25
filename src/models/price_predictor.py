"""
ML model for housing price prediction.
Uses processed property data to train and predict housing prices.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import logging

logger = logging.getLogger(__name__)

class HousingPricePredictor:
    """
    ML model for predicting housing prices based on property characteristics.
    """
    
    def __init__(self, model_type: str = 'random_forest'):
        """
        Initialize the price predictor.
        
        Args:
            model_type: Type of model to use ('random_forest', 'gradient_boosting', 'linear')
        """
        self.model_type = model_type
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = None
        self.feature_importance = None
        self.training_metrics = {}
        
    def prepare_features(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
        """
        Prepare features and target for training.
        
        Args:
            data: DataFrame with property data
            
        Returns:
            Tuple of (features, target)
        """
        # Select features for the model
        feature_columns = [
            'bedrooms', 'bathrooms', 'square_footage', 'year_built',
            'land_value', 'bldg_value', 'garage_sqft'
        ]
        
        # Create feature matrix
        X = data[feature_columns].copy()
        y = data['sale_price']
        
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
        X['total_sqft'] = X['square_footage'] + X['garage_sqft']
        
        # Store feature names
        self.feature_names = X.columns.tolist()
        
        return X, y
    
    def train(self, data: pd.DataFrame) -> Dict:
        """
        Train the price prediction model.
        
        Args:
            data: DataFrame with property data
            
        Returns:
            Dictionary with training metrics
        """
        try:
            # Prepare features and target
            X, y = self.prepare_features(data)
            
            if len(X) < 50:
                raise ValueError(f"Insufficient data for training: {len(X)} samples")
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Scale features
            X_train_scaled = self.scaler.fit_transform(X_train)
            X_test_scaled = self.scaler.transform(X_test)
            
            # Initialize model
            if self.model_type == 'random_forest':
                self.model = RandomForestRegressor(
                    n_estimators=100,
                    max_depth=10,
                    random_state=42,
                    n_jobs=-1
                )
            elif self.model_type == 'gradient_boosting':
                self.model = GradientBoostingRegressor(
                    n_estimators=100,
                    max_depth=6,
                    random_state=42
                )
            elif self.model_type == 'linear':
                self.model = LinearRegression()
            else:
                raise ValueError(f"Unknown model type: {self.model_type}")
            
            # Train model
            if self.model_type == 'linear':
                self.model.fit(X_train_scaled, y_train)
                y_pred = self.model.predict(X_test_scaled)
            else:
                self.model.fit(X_train, y_train)
                y_pred = self.model.predict(X_test)
            
            # Calculate metrics
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            rmse = np.sqrt(mse)
            r2 = r2_score(y_test, y_pred)
            
            # Calculate percentage errors
            mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
            
            # Store feature importance if available
            if hasattr(self.model, 'feature_importances_'):
                self.feature_importance = dict(zip(self.feature_names, self.model.feature_importances_))
            
            # Store training metrics
            self.training_metrics = {
                'mae': mae,
                'mse': mse,
                'rmse': rmse,
                'r2': r2,
                'mape': mape,
                'training_samples': len(X_train),
                'test_samples': len(X_test),
                'feature_count': len(self.feature_names)
            }
            
            logger.info(f"Model training completed. R²: {r2:.3f}, RMSE: ${rmse:,.0f}")
            
            return self.training_metrics
            
        except Exception as e:
            logger.error(f"Error training model: {e}")
            raise
    
    def predict(self, property_data: pd.DataFrame) -> np.ndarray:
        """
        Predict prices for new properties.
        
        Args:
            property_data: DataFrame with property features
            
        Returns:
            Array of predicted prices
        """
        if self.model is None:
            raise ValueError("Model must be trained before making predictions")
        
        try:
            # Prepare features
            X = property_data[self.feature_names].copy()
            X = X.fillna(X.median())
            
            # Scale features
            X_scaled = self.scaler.transform(X)
            
            # Make predictions
            if self.model_type == 'linear':
                predictions = self.model.predict(X_scaled)
            else:
                predictions = self.model.predict(X)
            
            return predictions
            
        except Exception as e:
            logger.error(f"Error making predictions: {e}")
            raise
    
    def predict_single_property(self, 
                               bedrooms: int,
                               bathrooms: float,
                               square_footage: int,
                               year_built: int,
                               land_value: Optional[int] = None,
                               bldg_value: Optional[int] = None,
                               garage_sqft: Optional[int] = None) -> Dict:
        """
        Predict price for a single property.
        
        Args:
            Property characteristics
            
        Returns:
            Dictionary with prediction and confidence
        """
        try:
            # Create property data
            property_data = pd.DataFrame([{
                'bedrooms': bedrooms,
                'bathrooms': bathrooms,
                'square_footage': square_footage,
                'year_built': year_built,
                'land_value': land_value or 0,
                'bldg_value': bldg_value or 0,
                'garage_sqft': garage_sqft or 0
            }])
            
            # Add engineered features
            property_data['price_per_sqft'] = 0  # Will be calculated during prediction
            property_data['total_bathrooms'] = bathrooms
            property_data['age'] = datetime.now().year - year_built
            property_data['land_to_building_ratio'] = (land_value or 0) / ((bldg_value or 0) + 1)
            property_data['total_sqft'] = square_footage + (garage_sqft or 0)
            
            # Make prediction
            predicted_price = self.predict(property_data)[0]
            
            # Calculate confidence based on model performance
            confidence = max(0.5, min(0.95, self.training_metrics.get('r2', 0.7)))
            
            return {
                'predicted_price': int(predicted_price),
                'confidence': confidence,
                'features_used': self.feature_names,
                'model_type': self.model_type
            }
            
        except Exception as e:
            logger.error(f"Error predicting single property: {e}")
            raise
    
    def save_model(self, filepath: str) -> None:
        """
        Save the trained model to disk.
        
        Args:
            filepath: Path to save the model
        """
        try:
            model_data = {
                'model': self.model,
                'scaler': self.scaler,
                'feature_names': self.feature_names,
                'feature_importance': self.feature_importance,
                'training_metrics': self.training_metrics,
                'model_type': self.model_type,
                'training_date': datetime.now().isoformat()
            }
            
            joblib.dump(model_data, filepath)
            logger.info(f"Model saved to {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving model: {e}")
            raise
    
    def load_model(self, filepath: str) -> None:
        """
        Load a trained model from disk.
        
        Args:
            filepath: Path to the saved model
        """
        try:
            model_data = joblib.load(filepath)
            
            self.model = model_data['model']
            self.scaler = model_data['scaler']
            self.feature_names = model_data['feature_names']
            self.feature_importance = model_data['feature_importance']
            self.training_metrics = model_data['training_metrics']
            self.model_type = model_data['model_type']
            
            logger.info(f"Model loaded from {filepath}")
            
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise
    
    def get_feature_importance(self) -> Dict:
        """
        Get feature importance scores.
        
        Returns:
            Dictionary of feature importance scores
        """
        if self.feature_importance is None:
            raise ValueError("Model must be trained to get feature importance")
        
        return self.feature_importance
    
    def get_training_metrics(self) -> Dict:
        """
        Get training metrics.
        
        Returns:
            Dictionary of training metrics
        """
        return self.training_metrics

def train_price_model(data: pd.DataFrame, 
                     model_type: str = 'random_forest',
                     save_path: Optional[str] = None) -> HousingPricePredictor:
    """
    Train a housing price prediction model.
    
    Args:
        data: DataFrame with property data
        model_type: Type of model to train
        save_path: Optional path to save the model
        
    Returns:
        Trained HousingPricePredictor instance
    """
    try:
        # Initialize predictor
        predictor = HousingPricePredictor(model_type=model_type)
        
        # Train model
        metrics = predictor.train(data)
        
        # Save model if path provided
        if save_path:
            predictor.save_model(save_path)
        
        logger.info(f"Price prediction model trained successfully")
        logger.info(f"Training metrics: {metrics}")
        
        return predictor
        
    except Exception as e:
        logger.error(f"Error training price model: {e}")
        raise 