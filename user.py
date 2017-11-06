class User(object):
   
    def __init__(self,firstname=None,lastname=None, email=None, password= None,categories = None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.categories = []
        self.userstore = {}
    
    def signup(self,firstname,lastname, email, password):
        if firstname in self.userstore:
            return "You already have an account with us...........Please login"

        else:
           self.userstore.update({firstname:password})


    def login(self, firstname, password):
        if firstname in userstore and self.userstore[firstname] == password:
           return "Welcome to Yummy recipes"
        else:
           return "Please enter the correct firstname and password or signup if you have no account"

    
    def add_category(self, category):
        if category in categories:
            return "Category already exists"
        else:
            self.categories.append(category)

    def delete_category(self, category):
        if category in categories:
            self.categories.remove(category)
        else:
            return "No category to delete"

    def view_categories(self,category):
        if category in categories:
            return self.categories
        else:
            return "No categories"