class Animal:
    def speaks(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")    
dog=Dog()
dog.speaks()            