import unittest
from main import _mult, read

class TestMult(unittest.TestCase):
    def test__min(self):
        self.assertEqual(24, _mult(read('text.txt')))

if __name__ == '__main__':
    unittest.main()
