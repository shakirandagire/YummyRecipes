import unittest

from user import User

class TestCategories(unittest.TestCase):
    def setUp(self):
        self.user = User ("firstname", "lastname", "email", "password")

    def test_to_add_category(self):
        self.user.add_category("chicken")
        self.assertEqual(self.user.view_categories(), ["chicken"], msg='Added recipe category')

    def test_delete_recipe_from_category(self):  
        self.user.add_category("chicken")
        self.user.delete_category("chicken")
        self.assertEqual(self.user.categories, [], msg='Category deleted')

    def test_view_recipe_in_category(self):
        self.user.add_category("chicken")
        self.assertEqual(self.user.view_categories(), ['chicken'], msg="Categories displayed")

if __name__ == '__main__':
    unittest.main()