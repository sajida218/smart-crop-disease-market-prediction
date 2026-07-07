from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from app.api.routes import router as prediction_router
from app.api.system import router as system_router
from app.api.analytics import router as analytics_router
from app.api.market import router as market_router

from app.utils.exceptions import (
    validation_exception_handler,
    internal_exception_handler
)

app = FastAPI(
    title="Smart Crop Disease Detection API",
    version="1.0.0",
    description="AI-powered backend for plant disease detection.",
    contact={
        "name": "Buddala Yashwant",
        "email": "yashwantbudhala27@gmail.com"
    },
    license_info={
        "name": "MIT"
    }
)

# ==========================
# CORS Configuration
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Exception Handlers
# ==========================
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    internal_exception_handler
)

# ==========================
# API Routers
# ==========================
app.include_router(
    prediction_router,
    prefix="/api/v1",
    tags=["Prediction"]
)

app.include_router(
    system_router,
    prefix="/api/v1",
    tags=["System"]
)

app.include_router(
    analytics_router,
    prefix="/api/v1",
    tags=["Analytics"]
)

app.include_router(
    market_router,
    prefix="/api/v1",
    tags=["Market"]
)

# ==========================
# Root Endpoint
# ==========================
@app.get("/")
def root():
    return {
        "success": True,
        "message": "Welcome to Smart Crop Disease Detection API",
        "version": "1.0.0"
    }