"""
conftest.py: It contents fixture functions used in tests.
"""

__author__ = "alvertogit"
__copyright__ = "Copyright 2018-2025"


import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app


@pytest.fixture
def app() -> Flask:
    """
    Create a Flask app instance for testing.

    Returns:
        flask.Flask: The Flask app instance.
    """

    app = create_app("testing")
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """
    Create a Flask test client for the app.

    Args:
        app (flask.Flask): The Flask app instance.

    Returns:
        flask.testing.FlaskClient: The Flask test client.
    """

    return app.test_client()
