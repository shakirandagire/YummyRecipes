class Categories:

    def __init__(self, categoryname):
        self.categoryname = categoryname
        self.recipe_store = {}

     
    def add_recipe(self, recipename, description):
        self.recipe_store[recipename] = description 
          
   
    def delete_recipe(self, recipename,description):
       if recipename in self.recipe_store:
            self.recipe_store.pop(recipename,description)

    
    def edit_recipe(self,recipename,new_recipename):
        if recipename in self.recipe_store:
            self.recipe_store[new_recipename] = self.recipe_store.pop(recipename)


    def view_recipes(self):
        return self.recipe_store

   