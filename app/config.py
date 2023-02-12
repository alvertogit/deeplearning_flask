"""
config.py: Configurations used by Flask server.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2018-2023"


import os

class DefaultConfig:
    if os.environ.get("SECRET_KEY"):
        SECRET_KEY = os.environ.get("SECRET_KEY")
    else:
        raise ValueError("SECRET KEY NOT FOUND!")

    MODEL_PATH = os.environ.get("MODEL_PATH") or "/app/mnist_model.h5"

    @staticmethod
    def init_app(app):
        print("PRODUCTION CONFIG")


class DevConfig(DefaultConfig):
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        print("DEVELOPMENT CONFIG")


class TestConfig(DefaultConfig):
    TESTING = True

    @classmethod
    def init_app(cls, app):
        print("TESTING CONFIG")


config = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": DefaultConfig,
    "default": DefaultConfig
}
