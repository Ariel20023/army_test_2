from scemess import Intel,Attack,Damage
from pydantic import ValidationError


class FieldTest:
    def __init__(self,logger,mongo,kafka_producer,cross_data,Update_from_air_force,attack_update):
        self.logger = logger
        self.mongo = mongo
        self.kafka_producer = kafka_producer
        self.cross_data = cross_data
        self.Update_from_air_force = Update_from_air_force
        self.attack_update = attack_update

    
    def Validation(self,package):
        package_validation = None
        error = None
        if package[0] == "Intel":

            try:
                package_validation = Intel.model_validate(package[1])
            except ValidationError as e:
                error = e
                self.logger.log("error",error)


            if package_validation is not None:
                self.cross_data.cross(package[1])
                
            else:
                pack = [package[1],str(error)]
                self.kafka_producer.send(pack)

            

        elif package[0] == "Attack":
            try:
                package_validation = Attack.model_validate(package[1])
            except ValidationError as e:
                error = e
                self.logger.log("error",error)

                if package_validation is not None:
                    self.Update_from_air_force.Update_doc(package[1])

                    
        else:
            try:
                package_validation = Damage.model_validate(package[1])
            except ValidationError as e:
                error = e
                self.logger.log("error",error)

                if package_validation is not None:
                    self.attack_update.update(package[1])


    