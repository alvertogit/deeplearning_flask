"""
test_app.py: It contents flask app tests.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2018-2023"


import pytest
import json
import sys

def test_index(client):
    response = client.get("/")
    # check response
    assert response.status_code == 200
    assert response.data == b"Deep Learning on Flask"

def test_api(client):
    # server REST API endpoint url and example image path
    SERVER_URL = "http://127.0.0.1:5000/api/predictlabel"
    IMAGE_PATH = "../app/static/4.jpg"

    # create payload with image for request
    image = open(IMAGE_PATH, "rb")
    payload = {"file": image}
    response = client.post(SERVER_URL, data=payload)

    # check response
    assert response.status_code == 200

    # JSON format
    try:
        json_response = json.loads(response.data.decode('utf8'))
    except ValueError as e:
        print(e)
        assert False

    # successful
    if json_response["success"]:
        # most probable label
        print(json_response["most_probable_label"])
        # predictions
        for dic in json_response["predictions"]:
            print("label {0} probability: {1}".format(dic["label"],dic["probability"]))
        
        assert json_response["most_probable_label"] == "4"
    # failed
    else:
        assert False
