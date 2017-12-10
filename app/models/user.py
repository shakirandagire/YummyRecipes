user_store = {}
    
class User:
    def __init__(self,username, password):
        self.username = username
        self.password = password 
        self.category_store = {}
    @classmethod    
    def sign_up(cls,username,password):
        if username and password:
            user_store[username]= User(username,password)
            return True
    @classmethod
    def log_in(cls,username,password):
        if username and password:
            if user_store.get(username):
                if  password == user_store[username].password:
                    return True

    def add_category(self, categoryname):
        if categoryname not in self.category_store and categoryname != "" and categoryname != " ":
            self.category_store[categoryname] = categoryname
            return True
        return False

    def edit_category(self, categoryname, new_categoryname):
        if categoryname in self.category_store:
            self.category_store[new_categoryname] =  self.category_store.pop(categoryname)
            return True
        return False

    def delete_category(self, categoryname):
        if categoryname in self.category_store:
            self.category_store.pop(categoryname)
            return True
        return False

    def view_categories(self):
        return self.category_store


    
