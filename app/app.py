# app/app.py

from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from app.preprocessing import preprocess_input_data, validate_input, model, scaler_x, scaler_y
import logging



def predict():
    try:
        # Terima data input dari request
        input_data = request.get_json()

        # Validasi input
        is_valid, message = validate_input(input_data)
        if not is_valid:
            return jsonify({"status": "error", "message": message})

        # Konversi input ke DataFrame
        input_df = pd.DataFrame(input_data, index=[0])
        print("Input Data Before Preprocessing:")
        print(input_df)

        # Preprocessing data
        processed_input = preprocess_input_data(input_df)
        print("Input Data After Preprocessing:")
        print(processed_input)

        # Prediksi harga
        prediction = model.predict(processed_input)
        predicted_price_scaled = prediction.reshape(-1, 1)
        predicted_price = scaler_y.inverse_transform(predicted_price_scaled)[0, 0]

        return jsonify({"status": "success", "predicted_price": predicted_price})
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify(
            {
                "status": "error",
                "message": "An error occurred while processing the input.",
            }
        )