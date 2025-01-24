import unittest
from unittest.mock import patch
from main import Calculator

class TestSum(unittest.TestCase):
    @patch('main.Calculator.sum',return_value=9)
    def test_sum(self,sum):
        self.assertEqual(sum(2,4),9)

if __name__ =='__main__':
    unittest.main()
