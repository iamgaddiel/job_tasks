from flask_restful import reqparse



template_crate_parser = reqparse.RequestParser()
template_crate_parser.add_argument('template_name', required=True, help="template_name is required")
template_crate_parser.add_argument('subject', required=True, help="subject is required")
template_crate_parser.add_argument('body', required=True, help="body is required")


template_put_parser = reqparse.RequestParser()
template_put_parser.add_argument('template_name')
template_put_parser.add_argument('subject')
template_put_parser.add_argument('body')
