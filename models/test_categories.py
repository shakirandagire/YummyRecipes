import unittest

from models.categories import Categories

class TestCategories(unittest.TestCase):
    def setUp(self):
       self.categories = Categories

    def test_to_add_category(self):
        self.categories.add_category("chicken")
        self.assertEqual(self.categories.view_categories(), ["chicken"], msg='Added recipe category')

    def test_delete_recipe_from_category(self):  
        self.categories.add_category("chicken")
        self.categories.delete_category("chicken")
        self.assertEqual(self.categories, [], msg='Category deleted')

    def test_view_recipe_in_category(self):
        self.categories.add_category("chicken")
        self.assertEqual(self.categories.view_categories(), ['chicken'], msg="Categories displayed")

if __name__ == '__main__':
    unittest.main()