import requests

from flask import Flask, jsonify
from requests.auth import HTTPDigestAuth
# from ipify import get_ip
# from ipify.exceptions import ConnectionError, ServiceError


from config import Config
from extensions import flask_jwt_ext


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Extensions
    flask_jwt_ext.init_app(app)

    # App blueprints
    from .template import template_bp
    from .auth import auth_bp


    # Blueprint registrations
    app.register_blueprint(template_bp)
    app.register_blueprint(auth_bp)

    atlas_group_id = app.config.get("ATLAS_GROUP_ID")
    atlas_api_public_key = app.config.get("ATLAS_PUBLIC_KEY")
    atlas_api_private_key = app.config.get("ATLAS_PRIVATE_KEY")
    # ip = requests.get('https://api.ipify.org').text
    # print(ip, '<----------- Ip address')

    print(atlas_api_private_key)

    # whitelist current IP adress via API Key on MongoDB Atlas
    print("Whitelisting...")

    # alternative to receive external ip-adress: https://checkip.amazonaws.com, https://ident.me 
    ip = requests.get('https://ident.me').text.strip()

    print(ip)

    resp = requests.post(
        "https://cloud.mongodb.com/api/atlas/v1.0/groups/{groupId}/accessList".format(groupId=atlas_group_id),
        # auth=HTTPDigestAuth(atlas_api_public_key, atlas_api_private_key),
        json={'ipAddress': ip, 'comment': 'From home'}
    )

    if resp.status_code in (200, 201):
        print("MongoDB Atlas whitelist request successful", flush=True)
    else:
        print(
            "MongoDB Atlas whitelist request problem: status code was {status_code}, content was {content}".format(
                status_code=resp.status_code, content=resp.content
            ),

            flush=True
        )



    @app.route('/', methods=['GET'])
    def root():
        return jsonify(data={"data": "Python Json Task"})
        

    return app

