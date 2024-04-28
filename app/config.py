"""
config.py: Configurations used by Flask server.
"""

__author__ = "alvertogit"
__copyright__ = "Copyright 2018-2024"


import os


class DefaultConfig:
    """
    Default configuration class.
    """

    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("SECRET KEY NOT FOUND!")

    MODEL_PATH = os.environ.get("MODEL_PATH") or "/app/mnist_model.keras"

    @staticmethod
    def init_app(app):
        """
        Initialize the application with the default configuration.
        """

        print("PRODUCTION CONFIG")


class DevConfig(DefaultConfig):
    """
    Development configuration class.
    """

    DEBUG = True

    @classmethod
    def init_app(cls, app):
        """
        Initialize the application with the development configuration.
        """

        print("DEVELOPMENT CONFIG")


class TestConfig(DefaultConfig):
    """
    Testing configuration class.
    """

    TESTING = True

    @classmethod
    def init_app(cls, app):
        """
        Initialize the application with the testing configuration.
        """

        print("TESTING CONFIG")


config = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": DefaultConfig,
    "default": DefaultConfig,
}
