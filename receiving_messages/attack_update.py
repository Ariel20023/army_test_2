




class AttackUpdate:
    def __init__(self,logger):
        self.logger = logger

    def update(self,data):
        exists = None
        exists = self.mongo.collection.find_one({"entity_id":data["entity_id"]})
        if exists is not None:
            self.mongo.collection.update_one(
                    {"entity_id":data["entity_id"]},
                    {"$set":data},
                    upsert = True
                )
            self.logger.log("info","update_one to mongo")
        