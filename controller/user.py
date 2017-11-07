class User:
    
    users_store = {}
   
    def __init__(self,firstname,lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.categories = {}
     

    @classmethod
    def login(cls,first_name, password):
        if first_name == cls.users_store[first_name].firstname:
            return True
        else:
            return False
        

    @classmethod   
    def signup(cls,firstname,lastname, email, password):
        new_user = cls(firstname,lastname,email,password)
        cls.users_store[new_user.firstname] =  new_user
        

    def add_category(self, category):
        if category not in self.categories.values():
            self.categories[category.name]= category

       
    def delete_category(self, category_name):
        if category_name in self.categories:
             self.categories[category_name] = None

        else:
             return ValueError   


    def view_categories(self):
        return self.categories.values()
    

