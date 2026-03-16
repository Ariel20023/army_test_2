from config import *
from consumer import *
from cross_data import *
from field_test import *
from haversine import *
from kafka_producer import *
from logger import *
from mongo import *
from ocestractor import *
from scemess import *
from Update_from_air_force import *
from attack_update import *
from field_test import *




def main():


    logger = Logger()
    #טוען נתונים
    config = Config()
    config.validate()

    #Class objects

    kafka_consumer = KafkaConsumer(config.bootstrap_servers,
                                   config.group_id,
                                   logger)
    

    kafka_producer = KafkaProducer(config.bootstrap_servers,
                                   logger)
    

    mongo = Mongo(config.mongo_url,
                  config.db_name,
                  config.collectiom_name,
                  logger)
    
    
    attack_update = AttackUpdate(logger)

    cross_data = CrossData(logger,mongo)

    update_from_air_force = UpdateFromAirForce(logger,mongo)

    field_test = FieldTest(logger,mongo,kafka_producer,cross_data,update_from_air_force,attack_update)

    #It's the engine that drives everything.
    ocestractor = Ocestractor(field_test)
    ocestractor.run()




if __name__ == "__main__":
    main()






