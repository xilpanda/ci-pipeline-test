import unittest
from calculator import add, subtract, multiply, divide, power

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-4, 2), -2)
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(5, 1), 5)

if __name__ == '__main__':
    unittest.main() 