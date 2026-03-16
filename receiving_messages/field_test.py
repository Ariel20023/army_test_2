from scemess import Intel,Attack,Damage
from pydantic import ValidationError
from cross_data import CrossData

class FieldTest:
    def __init__(self,logger,mongo,kafka_producer,cross_data):
        self.logger = logger
        self.mongo = mongo
        self.kafka_producer = kafka_producer
        self.cross_data = cross_data

    
    def Validation(self,package):
        package_validation = None
        error = None
        if package[0] == "Intel":

            try:
                package_validation = Intel.model_validate(package[1])
            except ValidationError as e:
                error = e

            if package_validation is not None:
                self.cross_data.cross(package[1])
                
            else:
                pack = [package[1],str(error)]
                self.kafka_producer.send(pack)

            

        # elif package[0] == "Attack":
        #     package_validation = Attack.model_validate(package[1])
        #     if package_validation:
        #         pass 
        

        # else:
        #     package_validation = Damage.model_validate(package[1])
        #     if package_validation:
        #         pass 


    