import unittest


class TestCategories(unittest.TestCase):
    def setUp(self):
        self.categories = Categories()

    def test_to_add_category(self):
        self.categories.append('chicken')
        self.assertEqual(self.categories.add_category, ['chicken', 'beef','rice'], msg='Add recipe to category')

    def test_delete_recipe_from_category(self):   
        self.categories.remove('chicken')
        self.assertEqual(self.categories.delete_category, ['chicken'], msg='Recipe deleted')

    def test_view_recipe_in_category(self):
        self.assertEqual(self.categories.viewcategories(), ['chicken','beef'],
                         msg="categories displayed")

if __name__ == '__main__':
    unittest.main()