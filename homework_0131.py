class animal:
    
    def __init__(self,name,HP):
        self.name = name
        self.HP= HP
        
    def __str__(self):
        return self.name
    
class Birds(animal):
    
    def bird(self):
        print("조류")
    
class mammalia(animal):
    
    def mam(self):
        print("포유류")

class chicken(Birds):
    def __init__(self,name,HP):
        super().__init__(name,HP)

class whale(mammalia):
    def __init__(self,name,HP):
        super().__init__(name,HP)

whalename=whale("고래",17)
print(whalename)