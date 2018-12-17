"""
test.py: It contents REST API system tests using requests.
"""

import json
import sys
import requests

def test_req():
    # server REST API endpoint url and example image path
    SERVER_URL = "http://127.0.0.1/predictlabel"
    IMAGE_PATH = "../api/static/4.jpg"

    # create payload with image for request
    image = open(IMAGE_PATH, "rb").read()
    payload = {"image": image}

    # post request
    try:
        req = requests.post(SERVER_URL, files=payload)
    except requests.exceptions.ConnectionError as e:
        print(e)
        req = None

    # JSON format
    if req is None:
        response = None
    else:
        try:
            response = req.json()
        except json.decoder.JSONDecodeError as e:
            print(e)
            response = None

    if response is None:
        assert False

    # successful
    if response["success"]:
        # most probable label
        print(response["most_probable_label"])
        # predictions
        for dic in response["predictions"]:
            print("label {0} probability: {1}".format(dic["label"],dic["probability"]))
        
        assert response["most_probable_label"] == "4"

    # failed
    else:
        assert False
