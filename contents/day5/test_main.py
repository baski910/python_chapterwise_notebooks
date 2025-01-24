import unittest
from main import Calculator

class TestSum(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.sum(2,4),6)

if __name__ == '__main__':
    unittest.main()
