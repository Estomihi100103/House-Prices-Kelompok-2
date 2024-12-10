from flask import render_template, request, jsonify, current_app
from flask import render_template, request, jsonify, current_app
from app.app import predict  



@current_app.route('/')
def index():
    return render_template('index.html')


@current_app.route('/predict', methods=['POST'])
def house_price_prediction():
    return predict()