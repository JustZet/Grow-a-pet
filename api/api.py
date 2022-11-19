import flask

from flask import Flask, jsonify, abort
from flask_restful import Resource, Api
from bson.objectid import ObjectId
from flask.json import JSONEncoder
from flask_cors import CORS


from routes.pets import Pets
from routes.pet import Pet

class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, ObjectId):
                return str(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
CORS(app)
api = Api(app)



api.add_resource(Pets, "/petsApi/pets")
api.add_resource(Pet, "/petsApi/pets/<id>")


if __name__ == "__main__":
    app.run(debug=True)
