class User(object):
    
    #init method is called every time a new object is created.
    def __init__(self, name, email):
        #these are instance variables
        self.name = name
        self.email = email
        self.logged = False

    #this is a method:
    def login(self):
        self.logged = True
        print self.name + "is logged in."
        return self

#creating new instance of the User class
new_user = User("Anna","anna@anna.com")
print new_user.email


michael = User()
anna = User()

print michael
print anna