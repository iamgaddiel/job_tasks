from flask_restful import reqparse


reg_parser = reqparse.RequestParser()
reg_parser.add_argument('first_name', type=str, help='first name is required', required=True)
reg_parser.add_argument('last_name', type=str, help='ast name is required', required=True)
reg_parser.add_argument('email', type=str, help='email is required', required=True)
reg_parser.add_argument('password', type=str, help='password is required', required=True)


login_parser = reqparse.RequestParser()
login_parser.add_argument('email', help='email is required', required=True)
login_parser.add_argument('password', help='email is required', required=True)
