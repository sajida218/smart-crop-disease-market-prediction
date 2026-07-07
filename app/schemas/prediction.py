from pydantic import BaseModel


class PredictionResponse(BaseModel):
    crop: str
    disease: str
    confidence: float
    cause: str
    symptoms: str
    prevention: str
    treatment: str


class ImageResponse(BaseModel):
    filename: str


class PredictionAPIResponse(BaseModel):
    success: bool
    prediction: PredictionResponse
    image: ImageResponse