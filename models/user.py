class User:
    
    user_store ={}
    category_store ={}
   
    def __init__(self,username, password):
        self.username = username
        self.password = password 
        self.category_store = {}       
        
    def sign_up(self,username,password):
        if username and password:
            self.user_store[username]= User(username,password)
            return True
    
    def log_in(self,username,password):
        if username and password:
            if self.user_store.get(username):
                if  password == self.user_store[username].password:
                    return True

    def add_category(self, categoryname):
        if categoryname not in self.category_store and categoryname != "" and categoryname != " ":
            self.category_store[categoryname] = categoryname
            return True
        return False

    def edit_category(self, categoryname, new_categoryname):
        if categoryname in self.category_store and new_categoryname != "" and new_categoryname!=" ":
            self.category_store[new_categoryname] = self.category_store.pop(categoryname)
            return True
        return False

    def delete_category(self, categoryname):
        if categoryname in self.category_store:
            self.category_store.pop(categoryname)
            return True
        return False

    def view_categories(self):
        return self.category_store


    
