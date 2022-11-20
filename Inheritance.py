# Point class

class Point:
    

    # initialize object
    def __init__(self, x, y):#constructor
        self.__x = x
        self.__y = y
        pass

    # getters and setters
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

#Colored Point Class 
        
class ColoredPoint(Point):
    
    'Child class of Point'

    # initialize object
    def __init__(self, x, y, colorName):
        self.__colorName = colorName
        super().__init__(x,y)

    # getters and setters
    def getColorName(self):
        return self.__colorName
    
    def setColoredName(self, colorName):
        self.__colorName = colorName


## Inheritance example

point = ColoredPoint(2,4,'red')

if isinstance(point, ColoredPoint):
    print("The color of the point is %s." % (point.getColorName()))
    print("It has coordinates x=%d and y=%d" % (point.getX(), point.getY()))



