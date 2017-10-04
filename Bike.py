class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def DisplayInfo(self):
        print "Price is $ " + str(self.price)
        print "Maximum speed is " + str(self.max_speed) + "mph"
        print "Total miles: " + str(self.miles) + " miles"

    def Ride(self):                         #creating functions for the class "Bike"
        print "Riding"
        self.miles = self.miles + 10
    
    def Reverse(self):
        print "Reverse Reverse"
        if self.miles >= 5:                 #prevents negative miles
            self.miles = self.miles - 5

Bike1 = Bike("200","22")
Bike1.Ride()
Bike1.Ride()
Bike1.Ride()
Bike1.Reverse()
Bike1.DisplayInfo()

Bike2 = Bike("300","30")
Bike2.Ride()
Bike2.Ride()
Bike2.Reverse()
Bike2.Reverse()
Bike2.DisplayInfo()

Bike3 = Bike("500", "50")
Bike3.Reverse()
Bike3.Reverse()
Bike3.Reverse()
Bike3.DisplayInfo()
