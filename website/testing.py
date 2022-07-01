import unittest

try:
    from views import __init__
    import unittest

except Exception as e:
    print("some modules are missing {} ".format(e))

    class FlaskTestCase(unittest.TestCase):

        def test_index(self):
            tester = self.__game1
            response = tester.get("/fo")
            statuscode = response.status_code
            self.assertIn("valorant", statuscode)
