from flask import Blueprint
from flask_restful import Api


template_bp = Blueprint('template', __name__)
template_api = Api(template_bp)


from .import views