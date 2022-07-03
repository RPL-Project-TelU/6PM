import unittest
from auth import app

class Testing (unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
    
    def tearDown(self):
        pass
    
    def test_root(self):
        response = self.app.get('/', follow_redirects= True)
        self.assertEqual(response.status_code, 200)
        

if __name__ == "__main__":
    unittest.main()