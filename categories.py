class Categories(object):

    def __init__(self, categoryname, recipes=None):
        self.categoryname = categoryname
        self.recipes = []

    def add_recipe(self, recipe):
        
        self.recipes.append(recipe)  
        
    def delete_recipe(self, recipe):
        if len(self.recipes) > 0 and recipe in self.recipes:
            self.recipes.remove(recipes)
        else:
            raise ValueError

    def view_recipes(self):
        return self.recipes