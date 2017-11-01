import unittest

from recipes import Recipes

class TestRecipes(unittest.TestCase):
    def setUp(self):
        self.recipes = Recipes()

    def test_add_recipe_to_category(self):
        self.recipes.append('chicken')
        self.recipes.append('beef')
        self.recipes.append('rice')
        self.assertEqual(self.recipes.addrecipe, ['chicken', 'beef','rice'], msg='Add recipe to category')

    def test_delete_recipe_from_category(self):   
        self.recipes.remove('chicken')
        self.assertEqual(self.recipes.deleterecipe, ['chicken'], msg='Recipe deleted')

    def test_view_recipe_in_category(self):
        self.assertEqual(self.recipes.viewrecipes(), ['chicken','beef'],
                         msg="Recipes displayed")

if __name__ == '__main__':
    unittest.main()
    