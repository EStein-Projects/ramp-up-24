import unittest

from adjacent_nodes_medium import is_adjacent
from virtual_dac_medium import V_DAC

class MediumsTester(unittest.TestCase):
    def test_adjacency(self):
        matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
        self.assertEqual(is_adjacent(matrix, 0, 1), True)
        self.assertEqual(is_adjacent(matrix, 0, 2), False)
        self.assertEqual(is_adjacent(matrix, 2, 1), True)

        matrix = [[0,1,0,1,1], [1,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]]
        self.assertEqual(is_adjacent(matrix, 0, 3), True)
        self.assertEqual(is_adjacent(matrix, 1, 4), False)
        self.assertEqual(is_adjacent(matrix, 3, 2), True)

    def test_adjacency(self):
        self.assertEqual(V_DAC(1023), 5)
        self.assertEqual(V_DAC(0), 0)
        self.assertEqual(V_DAC(500), 2.44)

if __name__ == '__main__':
    unittest.main()