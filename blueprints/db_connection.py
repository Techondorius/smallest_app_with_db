from flask import Flask, Blueprint
from flask_restful import Api, Resource

app = Blueprint('blueprints', __name__)
api = Api(app)

class noot(Resource):
    def get(self):
        return{'message' : 'noot'}

api.add_resource(noot, '/')