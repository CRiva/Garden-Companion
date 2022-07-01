from flask import Blueprint
from bson import json_util
from flask_restful import Api, Resource
from garden_companion_api.database import SessionLocal, engine
from garden_companion_api.db.models.Plant import Plant as PlantModel

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

session = SessionLocal()


class Plant(Resource):
    def get(self):
        plants = session.query(PlantModel).all()
        print(plants)
        return json_util.dumps(plants)
