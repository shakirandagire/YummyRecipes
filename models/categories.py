class Categories:
    
    category_store = {}

    def __init__(self, categoryname):
        self.categoryname = categoryname
        self.category_store = {}

    @classmethod
    def add_category(self, categoryname):
        if categoryname not in self.category_store.values() and categoryname != "":
            self.category_store[categoryname] = categoryname
            return True
        return False

    @classmethod
    def delete_category(cls, categoryname):
        if categoryname in cls.category_store:
            cls.category_store.pop(categoryname)

    @classmethod
    def edit_category(self,categoryname,new_categoryname):
        if categoryname in self.category_store:
            self.category_store[new_categoryname] = self.category_store.pop(categoryname)
            return True

    @classmethod
    def view_categories(self):
        return self.category_store
