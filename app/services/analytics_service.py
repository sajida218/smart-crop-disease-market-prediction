
import json
from collections import Counter
from datetime import datetime

HISTORY_FILE="history/predictions.json"

def get_analytics():
    try:
        with open(HISTORY_FILE,"r") as f:
            history=json.load(f)
    except:
        history=[]

    disease=Counter()
    crop=Counter()
    daily=Counter()
    confidence=[]

    for h in history:
        disease[h["disease"]]+=1
        crop[h["crop"]]+=1
        confidence.append(h["confidence"])
        day=h["timestamp"].split()[0]
        daily[day]+=1

    return {
        "success":True,
        "disease_distribution":dict(disease),
        "crop_distribution":dict(crop),
        "daily_predictions":dict(daily),
        "confidence_trend":confidence[-20:]
    }
