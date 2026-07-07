from tensorflow.keras.models import load_model
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "plant_disease_model.h5")

print("Loading model...")
model = load_model(MODEL_PATH)
print("Model loaded successfully!")