import numpy as np
from PIL import Image


def preprocess_image(image, target_size=(128, 128)):
    image = image.convert("RGB")
    image = image.resize(target_size)

    image_array = np.array(image, dtype=np.float32)

    image_array = image_array / 255.0

    image_array = np.expand_dims(image_array, axis=0)

    return image_array