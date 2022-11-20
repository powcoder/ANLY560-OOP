## Animal base class

class Animal:

    def makeSound(self):
        return "The animal makes sounds"

## Cat extends Animal

class Cat(Animal):

    #overriding
    def makeSound(self):
        return "The cat meows"
    
## Dog extends Animal

class Dog(Animal):

    def makeSound(self):
        return "The dog barks"
    

## polymorphism Example

myAnimal = Animal()
print("What does the animal do? %s. " % (myAnimal.makeSound()))
myCat = Cat()
print("What does the cat do?  %s. " % (myCat.makeSound()))
myDog = Dog()
print("What does the dog do?  %s. " % (myDog.makeSound()))