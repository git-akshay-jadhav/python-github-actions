import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Welcome to my Flask web application!')

    def test_about(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'This is a simple Flask web application created for demonstration purposes.')

if __name__ == '__main__':
    unittest.main()
