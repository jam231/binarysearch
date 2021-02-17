import unittest
import Solution as s

class SolutionTests(unittest.TestCase):
    def test_small(self):
        self.solution = s.Solution()
        input = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        output = self.solution.solve(input)
        self.assertEqual(output, 2)

    def test_single_water_cell(self):
        self.solution = s.Solution()
        input = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
        output = self.solution.solve(input)
        self.assertEqual(output, 4)


    def test_only_land(self):
        self.solution = s.Solution()
        input = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        output = self.solution.solve(input)
        self.assertEqual(output, -1)

    def test_only_water(self):
        self.solution = s.Solution()
        input = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        output = self.solution.solve(input)
        self.assertEqual(output, -1)



    
