import unittest

from discount_easy import dis
from stutter_easy import stutter

class EasysTester(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(dis(100, 75), 25)
        self.assertEqual(dis(211, 50), 105.5)
        self.assertEqual(dis(593, 61), 231.27)
    
    def test_stutter(self):
        actual_input, expected_output = ["increasing", "am"], [
            "in... in... increasing?", "am... am... am?"]
        for i, o in zip(actual_input, expected_output):
            self.assertEqual(stutter(i), o)

if __name__ == '__main__':
    unittest.main()