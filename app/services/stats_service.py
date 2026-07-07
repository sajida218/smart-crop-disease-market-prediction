import json
import os
from collections import Counter

HISTORY_FILE = "history/predictions.json"


def get_prediction_stats():
    # Check if history file exists
    if not os.path.exists(HISTORY_FILE):
        return {
            "total_predictions": 0,
            "healthy_predictions": 0,
            "diseased_predictions": 0,
            "most_detected_disease": "None",
            "average_confidence": 0,
            "last_prediction": None
        }

    # Load prediction history
    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    if len(history) == 0:
        return {
            "total_predictions": 0,
            "healthy_predictions": 0,
            "diseased_predictions": 0,
            "most_detected_disease": "None",
            "average_confidence": 0,
            "last_prediction": None
        }

    total_predictions = len(history)

    healthy_predictions = 0
    diseased_predictions = 0

    confidence_sum = 0
    disease_list = []

    for prediction in history:

        disease = prediction["disease"]
        confidence = prediction["confidence"]

        confidence_sum += confidence
        disease_list.append(disease)

        if "healthy" in disease.lower():
            healthy_predictions += 1
        else:
            diseased_predictions += 1

    average_confidence = round(confidence_sum / total_predictions, 2)

    disease_counter = Counter(disease_list)

    most_detected_disease = disease_counter.most_common(1)[0][0]

    last_prediction = history[-1]["timestamp"]

    return {
        "total_predictions": total_predictions,
        "healthy_predictions": healthy_predictions,
        "diseased_predictions": diseased_predictions,
        "most_detected_disease": most_detected_disease,
        "average_confidence": average_confidence,
        "last_prediction": last_prediction
    }