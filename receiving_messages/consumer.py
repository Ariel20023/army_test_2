import json

from confluent_kafka import Consumer



class KafkaConsumer:
    def __init__(self,bootstrap_servers,group_id,topic):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.topic = topic
        self.auto.offset.reset = "earliest"

        self.consumer_config = {
            "bootstrap.servers":self.bootstrap_servers,
            "group.id":self.group_id,
             "auto.offset.reset":self.auto.offset.reset
        }

        self.consumer = Consumer(self.consumer_config)

        self.consumer.subscribe([self.topic])

print("Consumer is running and subscribed to orders topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value)
        print(f"Received order: {order['quantity']} x {order['item']} from {order['user']}")
except KeyboardInterrupt:
    print("\n Stopping consumer")

finally:
    consumer.close()