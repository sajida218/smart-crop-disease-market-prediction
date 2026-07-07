import os
import uuid
from fastapi import UploadFile

from app.config import UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_image(file: UploadFile):
    extension = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    with open(filepath, "wb") as image:
        image.write(file.file.read())

    return filename, filepath