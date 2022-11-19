
from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, reqparse

import sys
sys.path.append("api")
from databases.mongodb import MongoDatabase
from databases.dbconfig import Databases


class Pets(Resource):
    """"""
    def get(self):
        db = MongoDatabase(db_config=Databases.pets)
        all_pets = db.find_tables({})
    
        pets = []
        
        for pet in all_pets:
            pets.append(dict(pet))
            
        numResults = len(pets)
        return jsonify({"allResultsNumber": numResults, "pets": pets})

