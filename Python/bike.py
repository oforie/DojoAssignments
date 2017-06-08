class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print "Price is $"+ str(self.price) 
        print "Riding at " + str(self.max_speed), " mph"
        print "You've traveled " + str(self.miles) + " miles so far"
       

    def ride(self):
        print "Riding"
        self.miles += 10
       

    def reverse(self):
        print "Reversing"
        if self.miles >=5:
            self.miles -=5


#instances
bike1 = Bike(120, 20)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(150, 25)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(200, 30)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()


