class User:
    
    users_store ={}
   
    def __init__(self,username, password):
        self.username = username
        self.password = password
        
    @classmethod
    def login(cls,username, password):
        
        if username == cls.users_store[username].username:
            return True
        else:
            return False
        
    @classmethod   
    def signup(cls,username, password):
        new_user = cls(username,password)
        cls.users_store[new_user.username] =  new_user
        

    
