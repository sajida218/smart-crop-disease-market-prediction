import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "ml", "plant_disease_model.h5")
CLASS_NAMES_PATH = os.path.join(BASE_DIR, "ml", "class_names.txt")

UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}