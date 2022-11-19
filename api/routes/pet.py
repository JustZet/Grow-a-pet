
from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, reqparse

import sys
sys.path.append("api")
from databases.mongodb import MongoDatabase
from databases.dbconfig import Databases


class Pet(Resource):
    """"""
    def get(self, id: int):
        db = MongoDatabase(db_config=Databases.pets)
        pet = db.find_table({"id": int(id)})
        
    
        if pet:
            pet_data = dict(pet)
            return jsonify(pet_data)
        else:
             abort(404, f"Pet {id} not found")
             