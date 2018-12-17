from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from .config import ConfigForDev
from flask_restplus import Api

db = SQLAlchemy()


def init_api():
    api = Api(version='1.0', title='API', description='REST API')

    from . import router

    api.add_namespace(router.ns_app, path="/tx")

    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)

    return blueprint


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(ConfigForDev())
    db.init_app(flask_app)
    flask_app.register_blueprint(init_api(), url_prefix='/api')
    return flask_app