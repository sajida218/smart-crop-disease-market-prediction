from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image

from app.schemas.prediction import PredictionAPIResponse
from app.services.predict_service import predict
from app.services.upload_service import save_image
from app.services.history_service import (
    save_prediction,
    get_prediction_history
)
from app.utils.file_validation import validate_file
from app.utils.logger import logger
from app.services.stats_service import get_prediction_stats

router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionAPIResponse,
    summary="Predict Plant Disease",
    description="Upload a plant leaf image and receive disease prediction."
)
async def predict_disease(file: UploadFile = File(...)):
    try:
        logger.info(f"Prediction request received: {file.filename}")

        # Validate uploaded file
        validate_file(file.filename)

        # Save uploaded image
        filename, filepath = save_image(file)

        # Open image
        image = Image.open(filepath)

        # Predict disease
        result = predict(image)

        # Save prediction history
        save_prediction(result, filename)

        # Add uploaded image information
        result["image"] = {
            "filename": filename
        }

        logger.info(
            f"Prediction Successful -> "
            f"{result['prediction']['disease']} "
            f"({result['prediction']['confidence']}%)"
        )

        return result

    except HTTPException as e:
        logger.error(e.detail)
        raise e

    except Exception as e:
        logger.exception("Prediction Failed")

        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please try again."
        )


@router.get(
    "/history",
    summary="Prediction History",
    description="Returns all saved prediction history."
)
def prediction_history():

    logger.info("Prediction history requested")

    history = get_prediction_history()

    return {
        "success": True,
        "total_predictions": len(history),
        "history": history
    }
@router.get(
    "/stats",
    summary="Prediction Statistics",
    description="Returns analytics of all predictions."
)
def prediction_stats():

    stats = get_prediction_stats()

    return {
        "success": True,
        "stats": stats
    }