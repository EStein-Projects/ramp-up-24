import unittest

from interview_hard import interview
from snake_max_hard import snakefill

class HardsTester(unittest.TestCase):
    def test_interview(self):
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20, 20], 120), 'qualified')
        self.assertEqual(interview([2, 3, 0, 6, 5, 12, 10, 18], 120), 'qualified')
        self.assertEqual(interview([2, 3, 8, 6, 5, 12, 10, 18], 64), 'qualified')
        self.assertEqual(interview([5, 5, 10, 10, 25, 15, 20, 20], 120), 'disqualified')
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20], 120), 'disqualified')
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20, 20], 130), 'disqualified')
        self.assertEqual(interview([5, 5, 10, 20, 15, 15, 20, 20], 140), 'disqualified')
    
    def test_snake(self):
        self.assertEqual(snakefill(3), 3)
        self.assertEqual(snakefill(6), 5)
        self.assertEqual(snakefill(1), 0)
        self.assertEqual(snakefill(900), 19)

if __name__ == '__main__':
    unittest.main()