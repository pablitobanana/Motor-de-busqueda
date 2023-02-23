import pymongo
from pymongo import MongoClient

def connection_mongo():
    try:
        client = MongoClient('localhost', 27017)
        db = client['motor']
        collection = db['urls']
        return collection
    except Exception as ex:
        raise ex
