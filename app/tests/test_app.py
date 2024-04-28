"""
test_app.py: It contents flask app tests.
"""

__author__ = "alvertogit"
__copyright__ = "Copyright 2018-2024"


import json


def test_index(client):
    """
    Test the index route.

    Args:
        client (flask.testing.FlaskClient): The Flask test client.
    """

    response = client.get("/")

    # assert response status
    assert response.status_code == 200

    # assert response data
    assert response.data == b"Deep Learning on Flask"


def test_api(client):
    """
    Test the API endpoint to predict the label of an uploaded image with the Deep Learning model.

    Args:
        client (flask.testing.FlaskClient): The Flask test client.
    """

    # server REST API endpoint url and example image path
    SERVER_URL = "http://127.0.0.1:5000/api/predictlabel"
    IMAGE_PATH = "../app/static/4.jpg"

    # create payload with image for request
    with open(IMAGE_PATH, "rb") as image:
        payload = {"file": image}
        response = client.post(SERVER_URL, data=payload)

        # assert response status
        assert response.status_code == 200

        # JSON format
        try:
            json_response = json.loads(response.data.decode("utf8"))
        except ValueError as e:
            print(e)
            exit(1)

        # successful
        if json_response["success"]:
            # most probable label
            print(json_response["most_probable_label"])

            # predictions
            for dic in json_response["predictions"]:
                print(f"label {dic['label']} probability: {dic['probability']}")

            # assert the most probable label is 4
            assert json_response["most_probable_label"] == "4"
        # failed
        else:
            raise AssertionError("API endpoint /predictlabel failed")
