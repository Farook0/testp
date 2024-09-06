import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post('/', data=dict(num1='5', num2='3', operation='add'))
        self.assertIn(b'8.0', response.data)

    def test_subtraction(self):
        response = self.app.post('/', data=dict(num1='10', num2='4', operation='subtract'))
        self.assertIn(b'6.0', response.data)

    def test_multiplication(self):
        response = self.app.post('/', data=dict(num1='6', num2='7', operation='multiply'))
        self.assertIn(b'42.0', response.data)

    def test_division(self):
        response = self.app.post('/', data=dict(num1='8', num2='2', operation='divide'))
        self.assertIn(b'4.0', response.data)

    def test_division_by_zero(self):
        response = self.app.post('/', data=dict(num1='8', num2='0', operation='divide'))
        self.assertIn(b'Infinity', response.data)

    def test_invalid_input(self):
        response = self.app.post('/', data=dict(num1='abc', num2='2', operation='add'))
        self.assertIn(b'Invalid input', response.data)

if __name__ == '__main__':
    unittest.main()
