from pymongo import mongoClient



class MongoConfig:
    def __init__(self,mongo_url,db_name,collectiom_name):
        self.client = mongoClient(mongo_url)
        self.db = self.client[db_name]
        self.collection = self.db[collectiom_name]





