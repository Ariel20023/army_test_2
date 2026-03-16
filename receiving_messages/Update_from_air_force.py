




class UpdateFromAirForce:
    def __init__(self,logger,mongo):
        self.logger = logger
        self.mongo = mongo

    def Update_doc(self,data):
        exists = None
        exists = self.mongo.collection.find_one({"entity_id":data["entity_id"]})
        if exists is not None:
            data["target_mode"] = "attacked"
            self.mongo.collection.update_one(
                    {"entity_id":data["entity_id"]},
                    {"$set":data},
                    upsert = True
                )
            self.logger.log("info","update_one to mongo")




