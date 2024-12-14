from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import pandas as pd
import numpy as np
import joblib
from sklearn.impute import SimpleImputer
import logging

logger = logging.getLogger(__name__)




# Load scaler dan model
scaler_x = joblib.load("app/models/scaler_x.pkl")
scaler_y = joblib.load("app/models/scaler_y.pkl")
model = joblib.load("app/models/house_price_model.pkl")


def preprocess_input_data(input_data):
    # Definisikan fitur yang sama persis dengan saat training
    required_columns = [
        "OverallQual",
        "GrLivArea",
        "GarageCars",
        "GarageArea",
        "TotalBsmtSF",
        "1stFlrSF",
        "FullBath",
        "TotRmsAbvGrd",
        "YearBuilt",
        "YearRemodAdd",
    ]

    # Pastikan input memiliki semua kolom yang diperlukan
    try:
        input_data = input_data[required_columns]
    except KeyError as e:
        raise ValueError(f"Missing required columns: {e}")

    # Konversi tipe data
    input_data = input_data.astype(
        {
            "OverallQual": "int64",
            "GrLivArea": "float64",
            "GarageCars": "float64",
            "GarageArea": "float64",
            "TotalBsmtSF": "float64",
            "1stFlrSF": "float64",
            "FullBath": "int64",
            "TotRmsAbvGrd": "int64",
            "YearBuilt": "int64",
            "YearRemodAdd": "int64",
        }
    )

    # Gunakan scaler yang sudah di-load
    try:
        scaled_input = scaler_x.transform(input_data)
    except Exception as e:
        logger.error(f"Error while scaling input data: {e}")
        raise

    return scaled_input

# validasi input data yang masuk
def validate_input(input_data):
    required_columns = [
        "OverallQual",
        "GrLivArea",
        "GarageCars",
        "GarageArea",
        "TotalBsmtSF",
        "1stFlrSF",
        "FullBath",
        "TotRmsAbvGrd",
        "YearBuilt",
        "YearRemodAdd",
    ]
    for col in required_columns:
        if col not in input_data:
            return False, f"Missing required column: {col}"
    return True, "All required columns are present"