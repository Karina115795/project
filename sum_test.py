import unittest
from main import _sum, read

class TestSum(unittest.TestCase):
    def test__min(self):
        self.assertEqual(10, _sum(read('text.txt')))

if __name__ == '__main__':
    unittest.main()
