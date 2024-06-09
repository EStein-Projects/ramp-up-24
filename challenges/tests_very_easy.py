import unittest

from how_edabit_works_very_easy import hello
from nextnum_very_easy import addition

class VeryEasysTester(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "hello edabit.com")
    
    def test_add1(self):
        self.assertEqual(addition(2), 3)
        self.assertEqual(addition(-9), -8)
        self.assertEqual(addition(0), 1)
        self.assertEqual(addition(-1), 0)

if __name__ == '__main__':
    unittest.main()