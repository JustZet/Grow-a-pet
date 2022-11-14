import flask

from flask import Flask, jsonify, abort
from flask_restful import Resource, Api
from bson.objectid import ObjectId
from flask.json import JSONEncoder
from flask_cors import CORS

from routes.pets.pets import Pets
import sys




app = Flask(__name__)
CORS(app)
api = Api(app)



api.add_resource(Pets, "/petsApi/pets")


if __name__ == "__main__":
    app.run(debug=True)
