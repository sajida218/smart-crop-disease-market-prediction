from fastapi import HTTPException
from app.config import ALLOWED_EXTENSIONS


def validate_file(filename):
    extension = filename.split(".")[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported image format."
        )