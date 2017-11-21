import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("shakira", "password")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

if __name__ == '__main__':
    unittest.main()



  