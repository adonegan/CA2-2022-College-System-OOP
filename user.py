import random
import string
import datetime as dt

# USER SUPERCLASS
class User:

    # CLASS VARIABLES
    email_address = ""
    name = ""
    password = ""
    date_registered = ""
    department = ""
    possible_departments = ["Computing", "Science", "Marketing", "Business", "Art"]

    # instance counter
    count_users = 0

    # INITIALISER
    def __init__(self, email_address, name):
        try:
            self.setEmailAddress(email_address)
            self.setName(name)
            self.setPassword()
            self.setDate()
        except Exception as e:
            raise Exception("The User object has not been created.")
        # increment every time an object is created from this class
        User.count_users += 1

    # call this method in main.py to see how many objects are created
    @classmethod
    def count_all_users(cls):
        return cls.count_users 

    # GETTERS
    # to call and return information
    def getEmailAddress(self):
        return self.email_address
    
    def getName(self):
        return self.name
    
    def getPassword(self):
        return self.password
    
    def getDateRegistered(self):
        return self.date_registered
    
    # SETTERS
    # to change, update and user error check
    def setEmailAddress(self, email_address):
        # format check needed
        if '@' not in email_address:
            raise Exception("{0} is not a valid email address.".format(email_address))
        elif email_address[-4:] != '.com':
            raise Exception("{0} is not a valid email address.".format(email_address))
        else:
            self.email_address = email_address

    def setName(self, name):
        if name == "":
            raise Exception("Name cannot be blank.")
        else:
            self.name = name

    def setPassword(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        self.password = password

    def setDate(self):
        date = dt.date.today()
        self.date_registered = date

    # PRINT USER DETAILS
    def print(self):
        print("Name: \t\t\t", self.getName())
        print("Email address: \t\t", self.getEmailAddress())
        print("Password: \t\t", self.getPassword())
        print("Date registered:\t", self.getDateRegistered())
