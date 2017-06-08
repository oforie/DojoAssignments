class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def tax(self):
        if self.price > 10000:
            self.tax = 0.15
        else: 
            self.tax = 0.12
        return self.tax

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) +"mph"
        print "Tax: " + str(self.tax)
        print "Mileage: " + str(self.mileage)
        print "Fuel: " + str(self.fuel)




car1 = Car(2000, 35, "full", 15) 
car1.tax()
car1.display_all()

car2 = Car(2100, 5, "kinda full", 95)
car2.tax()
car2.display_all()

car3 = Car(2500, 25, "empty", 25)
car3.tax()
car3.display_all()

car4 = Car(12000, 35, "almost empty", 15)
car4.tax()
car4.display_all()

car5 = Car(2000, 35, "definitely empty", 15)
car5.tax()
car5.display_all()

car6 = Car(15000, 35, "Call a tow-truck", 15)
car6.tax()
car6.display_all()