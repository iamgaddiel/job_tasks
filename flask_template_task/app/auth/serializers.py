from flask_restful import fields


registration_fields = {
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
}