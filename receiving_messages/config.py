import os


class Config:
    def __init__(self,logger):
        self.bootstrap_servers = os.getenv("bootstrap_servers")
        self.group_id = os.getenv("group_id")
        self.mongo_url = os.getenv("mongo_url")
        self.db_name = os.getenv("db_name")
        self.collectiom_name = os.getenv("collectiom_name")
        self.logger = logger


    def validate(self):
        missing = []
        if not self.bootstrap_servers:
            missing.append("bootstrap_servers")

        if not self.group_id:
            missing.append("group_id")

        if not self.mongo_url:
            missing.append("mongo_url")

        if not self.db_name:
            missing.append("db_name")

        if not self.collectiom_name:
            missing.append("collectiom_name")
        
        if missing:
            message = f"missing data:{",".join(missing)}"
            self.logger.log("error",(message))
            raise ValueError(message)
        self.logger.log("info","All environment variables exist")






