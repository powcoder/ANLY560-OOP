## Car class

class Car:
    __name = "newCar" #double underscore means private
    __topSpeed = 0.0 #double underscore means private

    def getName(self):#getter method
        return self.__name

    def getTopSpeedMPH(self):
        return self.__topSpeed
    
    def setName(self, newName):#setter method
        self.__name = newName

    def setTopSpeed(self, speedMPH):
        self.__topSpeed = speedMPH

    def getTopSpeedKPH(self):
        return self.__topSpeed * 1.609344

## Encapsulation example

# instantiate a car object
myCar = Car()

# set the name attribute
myCar.setName("Porsche Cayenne 4.8-litre V8")

# set the speed attribute
myCar.setTopSpeed(173.0)

# output the speed
print("%s top speed in MPH is %d" % (myCar.getName(), myCar.getTopSpeedMPH()))
print("%s top speed in KPH is %d" % (myCar.getName(), myCar.getTopSpeedKPH()))



