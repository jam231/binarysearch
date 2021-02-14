import unittest
import Solution
import Tree 

class SolutionTests(unittest.TestCase):
    def test_k_in_left(self):
        tree = Tree.Tree(
            3,
            Tree.Tree(2),
            Tree.Tree(4)
        )
        solution = Solution.Solution()
        self.assertEqual(solution.solve(tree, 2), 4)


    def test_k_in_right(self):
        tree = Tree.Tree(
            3,
            Tree.Tree(2),
            Tree.Tree(4)
        )
        solution = Solution.Solution()
        self.assertEqual(solution.solve(tree, 4), 2)


    
