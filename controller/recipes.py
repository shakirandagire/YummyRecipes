class Recipe:
    
    recipe_store = {}

    def __init__(self, recipename, description):     
        self.recipename = recipename
        self.description = description

    def add_recipe(self, recipe):
        if recipe not in self.recipe_store.values():
            self.recipe_store[self.recipename]= recipe
      
    def delete_recipe(self, recipe):
        if len(self.recipe_store) > 0 and recipe in self.recipe_store:
            del self.recipe_store[self.recipename]
        else:
            raise ValueError("No recipes in category")

    def view_recipes(self):
        return self.recipe_store

        
        

