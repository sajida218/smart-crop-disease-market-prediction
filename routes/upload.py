from flask import Blueprint, request
import os
from werkzeug.utils import secure_filename

upload_bp = Blueprint('upload', __name__)

UPLOAD_FOLDER = 'uploads'

@upload_bp.route('/upload', methods=['POST'])
def upload():

    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400

    file = request.files['image']

    if file.filename == '':
        return {"error": "No file selected"}, 400

    filename = secure_filename(file.filename)

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    return {
        "message": "Image uploaded successfully",
        "filename": filename
    }, 200