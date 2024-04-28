"""
api.py: api views used by Flask server.
"""

__author__ = "alvertogit"
__copyright__ = "Copyright 2018-2024"


import io

from flask import Blueprint, jsonify, request
from skimage.io import imread

from .model import current_app, np, preprocess_image

api = Blueprint("api", __name__)


@api.route("/predictlabel", methods=["POST"])
def predict():
    """
    Predict the label of an uploaded image with the Deep Learning model.

    Returns:
        dict: The JSON response with the prediction results dictionary.
    """

    result = {"success": False}

    if request.method == "POST" and request.files.get("file"):
        # read image as grayscale
        image_req = request.files["file"].read()
        request.files["file"].close()
        image = imread(io.BytesIO(image_req), as_gray=True)

        # preprocess the image for model
        preprocessed_image = preprocess_image(image)

        # classify the input image generating a list of predictions
        model = current_app.config["model"]
        predictions = model.predict(preprocessed_image)

        # add generated predictions to result
        result["predictions"] = [
            {"label": str(i), "probability": str(pred)} for i, pred in enumerate(predictions[0])
        ]
        result["most_probable_label"] = str(np.argmax(predictions[0]))
        result["success"] = True

    return jsonify(result)
