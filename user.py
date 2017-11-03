class User(object):
   
    def __init__(self,firstname=None,lastname=None, email=None, password= None,categories = None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.categories =  []

    def login(self, firstname, password):
        if firstname == self.firstname and password == self.password:
            return True
        else:
            return False

    def signup(self,firstname,lastname, email, password):
        if firstname == self.firstname and lastname == self.lastname and email == self.email and password == self.password:
            return True

        else:
            return False

    def add_category(self, categories):
        self.categories.append(category)

    def delete_category(self, categories):
        self.categories.remove(category)

    def view_categories(self):
        return self.categories