from validation_department import Intel,Attack,Damage



class FieldTest:
    def __init__(self,logger):
        self.logger = logger

    
    def test(self,package):
        if package[0] == "Intel":
            package_validation = Intel(**package[1])
            if package_validation:
                pass    


        elif package[0] == "Attack":
            package_validation = Attack(**package[1])
            if package_validation:
                pass 
        
        else:
            package_validation = Damage(**package[1])
            if package_validation:
                pass 


    