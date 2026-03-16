



class Ocestractor:
    def __init__(self,logger,fieldtest):
        self.logger = logger
        self.fieldtest = fieldtest
      


    def run(self):

        while True:
            package_from_Kafka = self.KafkaConsumer.consume()
            self.logger.log("info","Received a package from Kafka")

            self.FieldTest.Validation(package_from_Kafka)




