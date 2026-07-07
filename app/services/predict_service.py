import os
import numpy as np

from app.services.model_loader import model
from app.utils.image_processing import preprocess_image
from app.utils.disease_info import DISEASE_INFO

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CLASS_FILE = os.path.join(BASE_DIR, "ml", "class_names.txt")

with open(CLASS_FILE, "r") as f:
    CLASS_NAMES = [line.strip() for line in f.readlines()]


def predict(image):
    processed_image = preprocess_image(image)

    predictions = model.predict(processed_image, verbose=0)

    predicted_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions) * 100)

    class_name = CLASS_NAMES[predicted_index]

    disease_details = DISEASE_INFO.get(class_name, {})

    return {
        "success": True,
        "prediction": {
            "crop": disease_details.get("crop", "Unknown"),
            "disease": disease_details.get("disease", class_name),
            "confidence": round(confidence, 2),
            "cause": disease_details.get("cause", "N/A"),
            "symptoms": disease_details.get("symptoms", "N/A"),
            "prevention": disease_details.get("prevention", "N/A"),
            "treatment": disease_details.get("treatment", "N/A")
        }
    }