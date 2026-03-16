from haversine import haversine_km



class CrossData:
    def __init__(self,logger,mongo):
        self.logger = logger
        self.mongo = mongo

    

    def cross(self,data):
        exists = None
        exists = self.mongo.collection.find_one({"signal_id":data["signal_id"]})
        if exists is not None:
            if exists["reported_lat"] and exists["reported_lon"] and data["reported_lat"] and data["reported_lon"]:#בודק אם השדות הללו בכלל קיימים
                data["travel_distance"] = haversine_km(exists["reported_lat"],exists["reported_lon"],data["reported_lat"],data["reported_lon"])
                self.mongo.collection.update_one(
                    {"signal_id":data["signal_id"]},
                    {"$set":data},
                    upsert = True
                )
                self.logger.info("update_one to mongo")


        else:
            data["travel_distance"] = 0
            data["priority_level"] = 99
            self.mongo.collection.insert_one(data)
            self.logger.info("send to mongo")





