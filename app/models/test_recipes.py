import unittest

from models.recipes import Recipe

class TestRecipes(unittest.TestCase):
    def setUp(self):
        self.recipes = Recipe("Recipename","Recipe Description")
    def test_recipe_instanciation(self):
        self.assertIsInstance(self.recipes,Recipe)
