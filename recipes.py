class Recipes(object):

    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description

    def addrecipe(self, name, category,description):
        self.recipes.append(name)
        self.recipes.append(category)
        self.recipes.append(description)

    def deleterecipe(self, recipe):
        if len(self.recipe) > 0 and recipe in self.recipes:
            self.recipes.remove(recipe)
        else:
            raise ValueError

    def viewrecipes(self):
        return self.recipes
        