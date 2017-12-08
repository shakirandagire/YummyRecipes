class Categories:

    def __init__(self, categoryname, recipe_store = None):
        self.categoryname = categoryname
        self.recipe_store = {}
   
    def add_recipe(self, recipename, description):
        if not recipename in self.recipe_store:
            self.recipe_store[recipename] = description 
            # self.recipe_list.append(self.recipe_store)
            return True
        return False       
   
    def delete_recipe(self, recipename,description):
       if recipename in self.recipe_store:
            self.recipe_store.pop(recipename,description)
            return True

    
    def edit_recipe(self,recipename,new_recipename):
        if recipename in self.recipe_store:
            self.recipe_store[new_recipename] = self.recipe_store.pop(recipename)
            return True


    def view_recipes(self):
        return self.recipe_store

   