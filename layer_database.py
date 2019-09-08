import os
from pymongo import MongoClient


# enviroments
MONGODB_SERVER = os.environ.get('MONGO_SERVER','localhost')
MONGO_PORT     = os.environ.get('MONGO_PORT', 27017)
MONGO_DB_NAME  = os.environ.get('MONGO_DB_NAME', 'mongo_flask_db')

client = MongoClient(MONGODB_SERVER, MONGO_PORT, connect=False)

db = client[MONGO_DB_NAME]
collection_user = db['users']

# User Document for users collection
class User(object):
    def __init__(self):
        self.name = ""
        self.username = ""
        self.email = ""
        self.password = ""
