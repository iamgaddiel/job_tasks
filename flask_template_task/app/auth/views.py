import bson
import bcrypt

from flask import request, current_app
from flask_restful import Resource, marshal_with

from flask_jwt_extended import create_access_token



from . import auth_api
from .parsers import reg_parser, login_parser
from .serializers import registration_fields
from extensions import db



class Login(Resource):
    def post(self):
        login_req = login_parser.parse_args()

        # check database if user exits
        user = db.users.find_one({'email': login_req.get('email')})
        
        # check if user exits
        if not user:
            return {'message': 'user not found'}

        # get and check if password is valid
        if not bcrypt.checkpw(login_req.get('password').encode('UTF-8'), user.get('password')):
            return {'message': 'invalid login credential'}

        # return token if valid
        identity = f'{user.get("first_name")}_{user.get("last_name")}'
        access_token = create_access_token(identity=identity)
        return {'access_token': access_token}


class RegisterView(Resource):
    @marshal_with(registration_fields)
    def post(self):
        reg_req = reg_parser.parse_args()

        # encrypt user password
        reg_req['password'] = bcrypt.hashpw(reg_req.get('password').encode('UTF-8'), bcrypt.gensalt())

        # save user data to user_collection
        db.users.insert_one(reg_req)

        return reg_req, 201


auth_api.add_resource(Login, '/login')
auth_api.add_resource(RegisterView, '/register')
