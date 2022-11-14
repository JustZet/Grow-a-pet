
from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, reqparse
import sys

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
import json


class Pets(Resource):
    """"""
    def get(self):
        with open('C:\Users\fsflo\OneDrive\Documente\projects\Grow-a-pet\lib\api\routes\pets.json', 'r') as json_file:
            
            pets = json.load(json_file)
            return pets
    
with open('pets.json', 'r') as f: 
    print(f)