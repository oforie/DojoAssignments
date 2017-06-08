class Product(object):
     
     tax_rate = 1.10
     store_return = .20
     
     
    def __init__(self, item_name, weight, brand, cost, status):
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = For Sale
            
    def display_info(self):
        print "Name: " + str(self.item_name)
        print "Weight: " + str(self.weight) + "grams"
        print "Brand: " + str(self.brand)
        print "Cost: $ " + str(self.cost)
        print "Status: " + str(self.sell)

    def final_price(self):
        int(self.cost * self.tax_rate)
    return final_price

    def add_tax(self):
        final_price = int(self.cost * self.tax_rate)

        def sell(self):
        if final_price > self.cost:
            self.status = "sold"
        else:
            "For sale"
    return sell
    
    def item_return(self, reason):
        int(self.cost * self.store_return)
        

item1 = Product("Acetaminophen", 10, "Tylenol", 15)
item2 = Product("Amoxycillin", 16, "KinaPharma", 18)
item3 = Product("Paracetamol", 10, "Kaiser", 14)
item4 = Product("Pepto Bismol", 10, "Walgreens", 25)