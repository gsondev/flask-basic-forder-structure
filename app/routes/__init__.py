from flask import Blueprint

base_api = Blueprint('base_api', __name__)

from . import auth_routes
from . import welcome_route