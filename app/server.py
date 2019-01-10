"""
server.py: Run Flask server with Deep Learning model.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2019"


import os

from app import create_app

app = create_app(os.environ.get("FLASK_ENV"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
