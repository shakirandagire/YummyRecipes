class Recipe:
    
    recipe_store = {}

    def __init__(self, recipename, description):     
        self.recipename = recipename
        self.description = description
        self.recipe_store = {}

    @classmethod
    def add_recipe(self, recipename, description):
        self.recipe_store[recipename] = description 
          
    @classmethod  
    def delete_recipe(self, recipename,description):
       if recipename in self.recipe_store:
            self.recipe_store.pop(recipename,description)

    @classmethod
    def edit_recipe(self,recipename,new_recipename):
        if recipename in self.recipe_store:
            self.recipe_store[new_recipename] = self.recipe_store.pop(recipename)

    @classmethod
    def view_recipes(self):
        return self.recipe_store

