class User:
    
    users_store = {}
   
    def __init__(self,firstname=None,lastname=None, email=None, password=None, categories=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

        self.categories =  []
     

    @classmethod
    def login(cls,first_name, password):
        if first_name == cls.users_store[first_name].firstname:
            return True
        else:
            return False
        

    @classmethod   
    def signup(cls,firstname,lastname, email, password):
        new_user = cls(firstname,lastname,email,password)
        cls.users_store[new_user.firstname] =  cls(firstname,lastname,email,password)
        

    def add_category(self, category):
        self.categories.append(category)

    def delete_category(self, category):
        self.categories.remove(category)

    def view_categories(self):
        return self.categories