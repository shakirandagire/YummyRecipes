import unittest

from categories import Categories

class TestRecipes(unittest.TestCase):
    def setUp(self):
        self.categories = Categories("categoryname")

    def test_add_recipe(self):
        self.categories.add_recipe("chicken curry")
        self.assertEqual(self.categories.view_recipes(), ["chicken curry"], msg='Added recipe to category')

    def test_delete_recipe(self):  
        self.categories.add_recipe("chicken curry")
        self.categories.delete_recipe("chicken curry")
        self.assertEqual(self.categories.recipes, [], msg='Recipe deleted')

    def test_view_recipe(self):
        self.categories.add_recipe("chicken")
        self.assertEqual(self.categories.view_recipes(), ['chicken'], msg="Recipes in category displayed")

if __name__ == '__main__':
    unittest.main()