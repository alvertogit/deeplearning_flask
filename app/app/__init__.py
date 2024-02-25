"""
__init__.py: Flask server with Deep Learning model.
"""

__author__ = "alvertogit"
__copyright__ = "Copyright 2018-2024"


from config import config
from flask import Flask, render_template

from .model import init_model


def create_app(config_name="default"):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    with app.app_context():
        app.config["model"] = init_model()

    from .api import api

    app.register_blueprint(api, url_prefix="/api")

    @app.route("/dlflask", methods=["GET"])
    def dlflask():
        return render_template("dlflask.html")

    @app.route("/", methods=["GET"])
    def index():
        return "Deep Learning on Flask"

    return app
