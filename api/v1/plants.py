from flask import Blueprint
from flask.cli import with_appcontext
from bson import json_util
from flask_restful import Api, Resource
from garden_companion_api import db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class Plant(Resource):
    def get(self):
        plants = db.get_db().db.plants.find()
        print(plants)
        return json_util.dumps(plants)
