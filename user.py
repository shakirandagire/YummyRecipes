class User(object):
   
    def __init__(self,firstname,lastname, email, password, recipes=None ,categories = None):
        self.firstname = firstname
        self.email = email
        self.password = password
        self.recipes = recipes or []
        self.categories = categories or []

    def login(self, email, password):
        if email == self.email and password == self.password:
            return True
        else:
            return False

    def add_recipes_to_category(self, recipes):
        self.recipes.append(recipe)

    def delete_recipes_from_category(self, recipes):
        self.recipes.remove(recipe)

    def view_recipes_in_category(self):
        return self.recipes

    def add_category(self, categories):
        self.categories.append(category)

    def delete_category(self, categories):
        self.categories.remove(category)

    def view_categories(self):
        return self.categories