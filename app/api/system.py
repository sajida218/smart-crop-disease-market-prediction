from fastapi import APIRouter
from app.services.model_loader import model

router = APIRouter()


@router.get("/health")
def health():
    """
    Check whether the backend service is running.
    """
    return {
        "success": True,
        "status": "Healthy",
        "message": "Backend is running successfully"
    }


@router.get("/model-info")
def model_info():
    """
    Returns information about the loaded AI model.
    """
    return {
        "success": True,
        "model_name": "plant_disease_model.h5",
        "framework": "TensorFlow / Keras",
        "input_size": "128 x 128",
        "classes": 15,
        "model_loaded": model is not None
    }