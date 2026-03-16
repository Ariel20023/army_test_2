import json

from confluent_kafka import Consumer



class KafkaConsumer:
    def __init__(self,bootstrap_servers,group_id,topic,logger):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.topic = topic
        self.auto.offset.reset = "earliest"
        self.logger = logger

        self.consumer_config = {
            "bootstrap.servers":self.bootstrap_servers,
            "group.id":self.group_id,
             "auto.offset.reset":self.auto.offset.reset
        }

        self.consumer = Consumer(self.consumer_config)

        self.consumer.subscribe([self.topic])

    def consume(self):
        try:
            msg = self.consumer.poll(1.0)
            if msg is None:
                return None
        
            if msg.error():
                self.logger.error(f"Error: {msg.error()}")

            value = msg.value().decode("utf-8")
            order = json.loads(value)
            self.logger.info("The package has been received")
        except KeyboardInterrupt:
            print("\n Stopping consumer")

