from scemess import Intel,Attack,Damage


class FieldTest:
    def __init__(self,logger,mongo):
        self.logger = logger
        self.mongo = mongo

    
    def test(self,package):
        if package[0] == "Intel":
            package_validation = Intel(**package[1])
            if package_validation:
                self.mongo.send(package[1])
                    
        elif package[0] == "Attack":
            package_validation = Attack(**package[1])
            if package_validation:
                pass 
        
        else:
            package_validation = Damage(**package[1])
            if package_validation:
                pass 


    