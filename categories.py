class Categories(object):

    def __init__(self, name, description, categories=None):
        self.name = name
        self.description = description
        self.categories = []

    def add_category(self, category):
        self.categories.append(name)  
        self.categories.append(description)  
             
    def delete_category(self, category):
        if len(self.categories) > 0 and category in self.categories:
            self.categories.remove(category)
        else:
            raise ValueError

    def view_categories(self):
        return self.categories