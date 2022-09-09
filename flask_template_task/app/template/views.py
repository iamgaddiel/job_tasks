from flask_restful import Resource, marshal_with
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from extensions import db

from . import template_api
from .parsers import template_put_parser, template_crate_parser
from .serializers import template_serializer, template_get_serializer


# shows a single template and lets you delete a template
class TemplateGet(Resource):
    @marshal_with(template_get_serializer)
    def get(self, template_id):
        template = db.templates.find_one({'_id': ObjectId(template_id)})
        return template, 200

    @marshal_with(template_get_serializer)
    def delete(self, template_id):
        template = db.templates.find_one_and_delete(
            {'_id': ObjectId(template_id)})
        return template, 200

    @marshal_with(template_get_serializer)
    def put(self, template_id):
        put_req = template_put_parser.parse_args()
        db.templates.update_one(
            {'_id': ObjectId(template_id)},
            {
                '$setOnInsert': put_req,
                "$currentDate": {"lastModified": True},
            },
            upsert=True
        )

        template = db.templates.find_one({'_id': ObjectId(template_id)})
        return template


#  shows a list of all templates, and lets you POST to add new template
class TemplateListCreate(Resource):
    @marshal_with(template_get_serializer)
    def get(self):
        templates_query = list(db.templates.find())
        templates = loads(dumps(templates_query))
        return templates, 200

    @jwt_required()
    @marshal_with(template_serializer)
    def post(self):
        create_req = template_crate_parser.parse_args()
        db.templates.insert_one(create_req)
        return create_req, 201


template_api.add_resource(TemplateGet, '/template/<string:template_id>')
template_api.add_resource(TemplateListCreate, '/template')
