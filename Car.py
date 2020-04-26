class Car:
    # Properties
    color = ""
    brand = ""
    numer_of_wheels = 4
    number_of_seats = 4
    maxspeed = 0

    # Constructor
    def __init__(self, color, brand, numer_of_wheels, number_of_seats, maxspeed):
       # def __init__(self,xcolor,xbrand,xnumer_of_wheels,xnumber_of_seats,xmaxspeed):
        self.color = color
        self.brand = brand
        self.numer_of_wheels = numer_of_wheels
        self.number_of_seats = number_of_seats
        self.maxspeed = maxspeed

    # Create method set color
    def setcolor(self, x):
        self.color = x

    def setbrand(self, x):
        self.brand = x

    def setspeed(self, x):
        self.speed = x

    def printdata(self):
        print("Color of this car is ", self.color)
        print("Brand of this car is ", self.brand)
        print("Max speed of this car is ", self.maxspeed)

    # Deconstructor
    def __del__(self):
        print()
