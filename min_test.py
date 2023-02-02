import unittest
from main import _min, read

class TestMin(unittest.TestCase):
    def test__min(self):
        self.assertEqual(1, _min(read('text.txt')))

if __name__ == '__main__':
    unittest.main()
