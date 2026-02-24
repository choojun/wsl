from pymongo import MongoClient

# To replace with your connection string:
CONNECTION_STRING = "<your connection string"


class PyMongoUtils:
    
    def __init__(self, uri=CONNECTION_STRING):
        self.uri = uri    

    def get_database(self, database_name):
        client = MongoClient(self.uri)
        return client[database_name]
