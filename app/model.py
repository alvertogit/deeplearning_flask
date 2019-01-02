"""
model.py: Functions related to Deep Learning model based on Keras.
"""

__author__      = "alverto"
__copyright__   = "Copyright 2019"


from keras.models import load_model
from skimage import transform, util
import numpy as np

from flask import current_app


def init_model():
    """Function that loads Deep Learning model.
    Returns:
        model: Loaded Deep Learning model.
    """
    
    model = load_model(current_app.config["MODEL_NAME"])#'mnist_model.h5')
    model._make_predict_function()
    return model

def preprocess_image(image):
    """Function that preprocess image.
    Returns:
        image: Preprocessed image.
    """

    # invert grayscale image
    image = util.invert(image)
    # resize and reshape image for model
    image = transform.resize(image, (28,28), anti_aliasing=True, mode="constant")
    image = np.array(image)
    image = image.reshape((1,28*28))

    return image
