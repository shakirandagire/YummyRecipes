class User:
    
    user_store ={}
   
    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.category_store = {}
        
        
    @classmethod
    def sign_up(cls,username,password):
        if username and password:
            cls.user_store[username]= User(username,password)
            return True
    
    @classmethod
    def log_in(cls,username,password):
        if username and password:
            if cls.user_store.get(username):
                if  password == cls.user_store[username].password:
                    return True


    
