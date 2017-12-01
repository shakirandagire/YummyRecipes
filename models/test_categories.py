import unittest

from models.categories import Categories

class TestCategories(unittest.TestCase):
    def setUp(self):
       self.categories = Categories("title")
    
    def test_created_user(self):
        self.assertIsInstance(self.categories, Categories)

    def test_add_recipe(self):
        self.assertTrue(self.categories.add_recipe("meat balls","boil for one hour"))

    def test_recipe_exists(self):
        self.categories.add_recipe("matooke","description")
        self.assertEqual(self.categories.add_recipe("matooke","description"), False)

    def test_edit_recipe_recipe_successful(self):
        self.categories.add_recipe("maize Snacks",'description')
        self.assertEqual(self.categories.edit_recipe("maize Snacks","local foods"),True)
        
    def test_category_not_found(self):
        self.assertFalse(self.categories.delete_recipe("rice","description"), False)

    def test_delete_category(self):
        self.categories.add_recipe("maize Snacks","keep it dry and fresh")
        self.assertEqual(self.categories.delete_recipe("maize Snacks","keep it dry and fresh"),True)
        


if __name__ == '__main__':
    unittest.main()


