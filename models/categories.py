recipe_store = {}

class Categories:

    def __init__(self, categoryname):
        self.categoryname = categoryname
    
   
    def add_recipe(self, recipename, description):
        if not recipename in recipe_store:
            recipe_store[recipename] = description 
            return True
        return False

          
   
    def delete_recipe(self, recipename,description):
       if recipename in recipe_store:
            recipe_store.pop(recipename,description)
            return True

    
    def edit_recipe(self,recipename,new_recipename):
        if recipename in recipe_store:
            recipe_store[new_recipename] = recipe_store.pop(recipename)
            return True


    # def view_recipes(self):
    #     return recipe_store

   