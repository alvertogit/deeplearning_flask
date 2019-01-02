"""
test.py: It contents REST API system tests using requests.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2019"


import json
import sys
import requests

def test_req():
    # server REST API endpoint url and example image path
    SERVER_URL = "http://127.0.0.1/api/predictlabel"
    IMAGE_PATH = "../app/static/4.jpg"

    # create payload with image for request
    image = open(IMAGE_PATH, "rb").read()
    payload = {"image": image}

    # post request
    try:
        req = requests.post(SERVER_URL, files=payload)
    except requests.exceptions.ConnectionError as e:
        print(e)
        assert False

    # JSON format
    try:
        response = req.json()
    except json.decoder.JSONDecodeError as e:
        print(e)
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
