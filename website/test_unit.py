import unittest
from auth import get_dark
from __init__ import create_app

class TestUnit(unittest.TestCase):
    
    def test_get_dark(self):
        dark_mode = get_dark()
        self.assertEqual(dark_mode, "off")
    def test_login_page(self):
        app = create_app()
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(b'Login' in response.data)

if __name__ == '__main__':
    unittest.main()