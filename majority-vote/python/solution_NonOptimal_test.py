import unittest
import Solution_NonOptimal as s

class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = s.Solution()

    def test_empty(self):
        self.assertEqual(self.solution.solve([]), -1)

    def test_single(self):
        self.assertEqual(self.solution.solve([2]), 2)
    
    def test_unique_elements(self):
        output = self.solution.solve(list(range(10)))
        self.assertEqual(output, -1)

    def test_every_element_exactly_half(self):
        output = self.solution.solve([1,2,1,2,1,2])
        self.assertEqual(output, -1)

    def test_majority(self):
        output = self.solution.solve([1,1,1,1,2,2,2])
        self.assertEqual(output, 1)
