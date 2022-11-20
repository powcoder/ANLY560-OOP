# Employee abstract base class

# import needed module
from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, paymentPerHour):
        self.__name = name
        self.__paymentPerHour = paymentPerHour
        super().__init__()
        

    @abstractmethod
    def calculateSalary(self):
        pass

    def getName(self):#getter
        return self.__name

    def setName(self, name):#setter
        self.__name = name

    def getPaymentPerHour(self):
        return self.__paymentPerHour

    def setPaymentPerHour(self, paymentPerHour):
        self.__paymentPerHour = paymentPerHour

## FullTimeEmployee implementation of abstract Employee

class FullTimeEmployee(Employee):

    def calculateSalary(self):
        return super().getPaymentPerHour() * 8

## Contractor implementation of abstract Employee

class Contractor(Employee):

    def __init__(self, name, paymentPerHour, workingHours):
        self.__workingHours = workingHours
        super().__init__(name, paymentPerHour)
        
    def calculateSalary(self):
        return super().getPaymentPerHour() * self.__workingHours

# start with full time employee

# instantiate a full time employee named Mickey Mouse
# who earns $20 per hour
fte = FullTimeEmployee("Mickey Mouse", 20)

print("Employee named %s is a full time employee and gets $%d per hour." % (fte.getName(), fte.getPaymentPerHour()))

print("%s has a one-day salary of $%d" % (fte.getName(), fte.calculateSalary()))

# next, the contractor

# instantiate a contractor named Donald Duck
# who earns $25/hour and works 100 hours
c = Contractor("Donald Duck", 25, 100)

print("Employee named %s is a contractor and gets $%d per hour." % (c.getName(), c.getPaymentPerHour()))

print("%s has a salary of $%d" % (c.getName(), c.calculateSalary()))





