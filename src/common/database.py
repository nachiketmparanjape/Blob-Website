import pymongo

class Database(object):
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    @staticmethod
    def initialize() -> object:
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: object, query: object) -> object:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: object, query: object) -> object:
        return Database.DATABASE[collection].find_one(query)