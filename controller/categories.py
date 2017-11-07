class Categories(object):

    def __init__(self, categoryname):
        self.categoryname = categoryname
        
        self.recipes = []

    def add_recipe(self, recipe):
        
        self.recipes.append(recipe)  
        
    def delete_recipe(self, recipe):
        if len(self.recipes) > 0 and recipe in self.recipes:
            self.recipes.remove(recipe)
        else:
            raise ValueError("No recipes in category")

    def view_recipes(self):
        return self.recipes