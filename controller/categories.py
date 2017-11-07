class Categories(object):

    def __init__(self, categoryname):
        self.categoryname = categoryname
       
        self.recipes = {}

    def add_recipe(self, recipe):
        if recipe not in self.recipes.values():
            self.recipes[recipe.recipename]= recipe




        
    def delete_recipe(self, recipe):
        if len(self.recipes) > 0 and recipe in self.recipes:
            del self.recipes[recipe.name]
        else:
            raise ValueError("No recipes in category")

    def view_recipes(self):
        return self.recipes