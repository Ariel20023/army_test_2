from pymongo import mongoClient



class Mongo:
    def __init__(self,mongo_url,db_name,collectiom_name,logger):
        self.client = mongoClient(mongo_url)
        self.db = self.client[db_name]
        self.collection = self.db[collectiom_name]
        self.logger = logger

    
    
    def send_to_mongo(self,data):
        self.collection.insert_one(data)
        self.logger.info("send to mongo")









