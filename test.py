from app import app

import unittest


class MyTest(unittest.TestCase):

    def test_home(self):
        test = app.test_client(self)
        response = test.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_dashboard(self):
        test = app.test_client(self)
        response = test.get('/dashboard', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_categories(self):
        test = app.test_client(self)
        response = test.get('/categories', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_addrecipe(self):
        test = app.test_client(self)
        response = test.get('/addrecipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        


if __name__ == '__main__':
    unittest.main()