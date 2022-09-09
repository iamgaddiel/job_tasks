from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

import pymongo
from pymongo import MongoClient


flask_jwt_ext = JWTManager()


db_client = MongoClient("mongodb+srv://iamgaddiel:iamgaddiel@tempaltecluster.nrhzd2g.mongodb.net/?retryWrites=true&w=majority")
db = db_client['TempalteCluster']