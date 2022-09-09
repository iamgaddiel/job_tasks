from flask_restful import fields


template_serializer = {
    'template_name': fields.String,
    'subject': fields.String,
    'body': fields.String
}


template_get_serializer = {
    '_id': fields.String,
    'template_name': fields.String,
    'subject': fields.String,
    'body': fields.String
}