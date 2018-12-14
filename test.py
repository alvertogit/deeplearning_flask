"""
test.py: It contents a REST API test example using requests.
"""

import requests

# server REST API endpoint url and example image path
SERVER_URL = "http://127.0.0.1/predictlabel"
IMAGE_PATH = "static/4.jpg"

# create payload with image for request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# post request
req = requests.post(SERVER_URL, files=payload).json()

# successful
if req["success"]:
    # most probable label
    print("most probable label: {0}".format(req["most_probable_label"]))
    # predictions
    for dic in req["predictions"]:
        print("label {0} probability: {1}".format(dic["label"],dic["probability"]))

# failed
else:
    print("Request failed")
