"""
conftest.py: It contents fixture functions used in tests.
"""

__author__ = "alvertogit"
__copyright__ = "Copyright 2018-2024"


import pytest

from app import create_app


@pytest.fixture
def app():
    app = create_app("testing")
    return app


@pytest.fixture
def client(app):
    return app.test_client()
