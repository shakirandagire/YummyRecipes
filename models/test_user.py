import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("shakira", "password")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

    def test_addcategory(self):
        self.assertEqual(self.user.add_category("lunch"),
                         True)

    def test_addcategoryname_exists(self):
        self.user.add_category("brunch")
        self.assertEqual(self.user.add_category("brunch"),
                         False)

    def test_editcategory(self):
        self.user.add_category("dinner")
        self.assertEqual(self.user.edit_category("snacks", "cookies"), False)

    def test_deletecategory(self):
        self.user.add_category("breakfast")
        self.assertEqual(self.user.delete_category("breakfast"),
                         True)


if __name__ == '__main__':
    unittest.main()



  