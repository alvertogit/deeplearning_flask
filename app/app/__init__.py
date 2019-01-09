"""
__init__.py: Flask server with Deep Learning model.
"""

__author__      = "alverto"
__copyright__   = "Copyright 2019"


from flask import Flask, render_template

from config import config
from .model import init_model

def create_app(config_name="default"):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    with app.app_context():
        app.config["model"] = init_model()

    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
