"""
server.py: Run Flask server with Deep Learning model.
"""

__author__ = "alvertogit"
__copyright__ = "Copyright 2018-2024"


from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
