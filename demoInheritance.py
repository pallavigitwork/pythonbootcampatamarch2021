
class Animal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
                
    
    def printBreath(self):
        print("yes")

class LandAnimal(Animal):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def printWalk(self):
        print("yes")
       
class WaterAnimal(Animal):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    
    def printSwim(self):
        print("yes")


class Amphibian(LandAnimal,WaterAnimal):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    
    def printAmazing(self):
        print("yes")

water=WaterAnimal(1,2)
water.printBreath()
water.printSwim()

land=LandAnimal(2,3,4)
land.printWalk()
land.printBreath()

anm = Animal(3,4)
anm.printBreath()


