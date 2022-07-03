import unittest
from flask import Flask
from dark_mode import get_dark
from configparser import ConfigParser
import __init__

class TestUnit(unittest.TestCase):

    def test_get_dark(self):
        result = ConfigParser()
        result.read('website/config.ini')
        dark_mode = get_dark()
        self.assertEqual(dark_mode, result['dark']['status'])
    
    def test_login_page(self):
        app = __init__.create_app
        tester = app.test_client(self)
        response = tester.get("/login")
        assert b"Login" in response.data

if __name__ == '__main__':
    unittest.main()