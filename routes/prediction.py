from flask import Blueprint, request
import random
from database.database import get_connection

prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route('/predict', methods=['POST'])
def predict():

    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400

    file = request.files['image']

    diseases = [
        "Tomato Early Blight",
        "Tomato Late Blight",
        "Healthy Leaf",
        "Bacterial Spot",
        "Leaf Mold"
    ]

    disease = random.choice(diseases)
    confidence = round(random.uniform(85, 99), 2)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions
    (image_name, disease_name, confidence)
    VALUES (?, ?, ?)
    """, (file.filename, disease, confidence))

    conn.commit()
    conn.close()

    return {
        "success": True,
        "filename": file.filename,
        "disease": disease,
        "confidence": confidence
    }
@prediction_bp.route('/history', methods=['GET'])
def history():

    conn = sqlite3.connect('database/crop.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions")

    rows = cursor.fetchall()

    conn.close()

    return {"history": rows}