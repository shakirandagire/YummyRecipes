user_store = {}
category_store = {}    
class User:
    def __init__(self,username, password):
        self.username = username
        self.password = password 
           
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
        if categoryname not in category_store and categoryname != "" and categoryname != " ":
            category_store[categoryname] = categoryname
            return True
        return False

    def edit_category(self, categoryname, new_categoryname):
        if categoryname in category_store:
            category_store[new_categoryname] =  category_store.pop(categoryname)
            return True
        return False

    @classmethod
    def delete_category(cls, categoryname):
        if categoryname in category_store:
            category_store.pop(categoryname)
            return True
        return False

    def view_categories(self):
        return category_store


    
