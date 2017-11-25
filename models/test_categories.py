import unittest

from categories import Categories

class TestCategories(unittest.TestCase):
    def setUp(self):
       self.categories = Categories

    def test_add_category(self):
        self.assertEqual(self.categories.add_category("lunch"),"recipe category is added succesfully")

    def test_category_exists(self):
        self.categories.add_category("lunch")
        self.assertEqual(self.categories.add_category("lunch"), "recipe category already exists")

    def test_edit_recipe_category_successful(self):
        self.categories.add_category("Snacks")
        self.assertEqual(self.categories.edit_category("Snacks","local foods"),"recipe_category not found")
        
    def test_category_not_found(self):
        self.assertEqual(self.categories.delete_category("dinner"), "category does not exist")

    def test_delete_category(self):
        self.assertEqual(self.categories.delete_category(""),"category deleted")
        
    def test_view_category(self):
        self.assertEqual(self.categories.view_categories(), "No categories found")


if __name__ == '__main__':
    unittest.main()


