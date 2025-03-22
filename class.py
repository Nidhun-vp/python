class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"{self.name} say Woof!")    
        
        
 #object created
dogobject=Dog("john","GermanShipard") 
dogobject.bark() #calling method
       