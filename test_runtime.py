import unittest
from main import divide

class TestRuntimeErrors(unittest.TestCase):
    def test_divide(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
