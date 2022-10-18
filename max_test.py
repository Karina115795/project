import unittest
from main import _max, read

class TestMax(unittest.TestCase):
    def test__min(self):
        self.assertEqual(4, _max(read('text.txt')))

if __name__ == '__main__':
    unittest.main()
