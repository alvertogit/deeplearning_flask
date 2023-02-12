"""
api.py: api views used by Flask server.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2018-2023"


from flask import Blueprint, jsonify, request

from skimage.io import imread
import io

from .model import *


api = Blueprint('api', __name__)

@api.route("/predictlabel", methods=["POST"])
def predict():
    # result dictionary that will be returned from the view
    result = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == "POST":
        if request.files.get("file"):
            # read image as grayscale
            image_req = request.files["file"].read()
            request.files["file"].close()
            image = imread(io.BytesIO(image_req), as_gray=True)

            # preprocess the image for model
            preprocessed_image = preprocess_image(image)

            # classify the input image generating a list of predictions
            model = current_app.config["model"]
            preds = model.predict(preprocessed_image)
            
            # add generated predictions to result
            result["predictions"] = []

            for i in range(0,10):
                pred = {"label": str(i), "probability": str(preds[0][i])}
                result["predictions"].append(pred)

            result["most_probable_label"] = str(np.argmax(preds[0]))

            # indicate that the request was a success
            result["success"] = True

    # return result dictionary as JSON response to client
    return jsonify(result)
