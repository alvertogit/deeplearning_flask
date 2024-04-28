"""
model.py: Functions related to Deep Learning model based on Keras.
"""

__author__ = "alvertogit"
__copyright__ = "Copyright 2018-2024"


import numpy as np
from flask import current_app
from skimage import transform, util
from tensorflow.keras.models import load_model


def init_model():
    """
    Load the pre-trained Deep Learning model.

    Returns:
        model (tensorflow.keras.Model): The loaded Deep Learning model.
    """

    model = load_model(current_app.config["MODEL_PATH"])
    model.make_predict_function()
    return model


def preprocess_image(image):
    """
    Preprocess an image for the Deep Learning model.

    Args:
        image (numpy.ndarray): The input image.

    Returns:
        preprocessed_image (numpy.ndarray): The preprocessed image.
    """

    # invert grayscale image
    inverted_image = util.invert(image)

    # resize and reshape image
    resized_image = transform.resize(inverted_image, (28, 28), anti_aliasing=True, mode="constant")
    resized_image = np.array(resized_image)
    preprocessed_image = resized_image.reshape((1, 28 * 28))

    return preprocessed_image
