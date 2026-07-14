import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "crop_disease_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)

classes = [
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___healthy"
]

def predict_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction) * 100)

    return {
        "disease": classes[class_index],
        "confidence": round(confidence, 2)
    }