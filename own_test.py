import unittest
import math

class TestFact(unittest.TestCase):
    def test__min(self):
        self.assertEqual(2, math.factorial(2))
        self.assertEqual(6, math.factorial(3))
        self.assertEqual(24, math.factorial(4))

if __name__ == '__main__':
    unittest.main()
