class Categories:
    
    category_store = {}

    def __init__(self, categoryname):
        self.categoryname = categoryname
        self.category_store = {}

    @classmethod
    def add_category(self, categoryname):
        # if category not in self.category_store.values():
        self.category_store[categoryname] = categoryname

    @classmethod
    def delete_category(self, categoryname):
        if categoryname in self.category_store:
            self.category_store.pop(categoryname)

    @classmethod
    def edit_category(self,categoryname,new_categoryname):
        if categoryname in self.category_store:
            self.category_store[categoryname] = new_categoryname

    @classmethod
    def view_categories(self):
        return self.category_store


    
    
