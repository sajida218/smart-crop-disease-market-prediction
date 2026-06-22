from flask import Blueprint, request, jsonify
from backend.predict import predict_image
import os

prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route('/predict', methods=['POST'])
def predict():

    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    upload_path = "temp.jpg"
    file.save(upload_path)

    result = predict_image(upload_path)

    os.remove(upload_path)

    return jsonify(result)