import json
import uuid
from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self,bootstrap_servers,logger):
        self.topic = "intel_signals_dlq"
        self.logger = logger
        self.producer = Producer({
            "bootstrap.servers":bootstrap_servers
        })



    def send(self,event:dict):
        value = json.dumps(event).encode("utf-8")
        self.logger.info("sending to kafka")

        self.producer.produce(
                topic=self.topic,
                value=value,
             )
        self.logger.info("The submission was successful")

        