"""
__init__.py: api views init.
"""

__author__      = "alverto"
__copyright__   = "Copyright 2019"


from flask import Blueprint

api = Blueprint('api', __name__)

from . import views
