import json
import os
from datetime import datetime

HISTORY_DIR = "history"
HISTORY_FILE = os.path.join(HISTORY_DIR, "predictions.json")

os.makedirs(HISTORY_DIR, exist_ok=True)

if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as file:
        json.dump([], file)


def save_prediction(result, filename):
    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    history.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "image": filename,
        "crop": result["prediction"]["crop"],
        "disease": result["prediction"]["disease"],
        "confidence": result["prediction"]["confidence"]
    })

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def get_prediction_history():
    with open(HISTORY_FILE, "r") as file:
        return json.load(file)