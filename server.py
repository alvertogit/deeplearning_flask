"""
server.py: Flask server with Deep Learning model based on Keras.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2018"

from flask import Flask, render_template, jsonify, request
from keras.models import load_model
from skimage import transform, util
from skimage.io import imread
import numpy as np
import os, io

app = Flask(__name__)
model = load_model('mnist_model.h5')
model._make_predict_function()

def preprocess_image(image):
    # invert grayscale image
    image = util.invert(image)
    # resize and reshape image for model
    image = transform.resize(image, (28,28), anti_aliasing=True, mode="constant")
    image = np.array(image)
    image = image.reshape((1,28*28))

    return image

@app.route("/predictlabel", methods=["POST"])
def predict():
    # result dictionary that will be returned from the view
    result = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == "POST":
        if request.files.get("image"):
            # read image as grayscale
            image_req = request.files["image"].read()
            image = imread(io.BytesIO(image_req), as_gray=True)

            # preprocess the image for model
            preprocessed_image = preprocess_image(image)

            # classify the input image generating a list of predictions
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


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
