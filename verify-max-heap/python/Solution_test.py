import unittest
import Solution

class TestSolution(unittest.TestCase):
    def test_empty(self):
        s = Solution.Solution()
        self.assertTrue(s.solve([]))

    def test_single_element(self):
        s = Solution.Solution()
        self.assertTrue(s.solve([1]))

    def test_full_heap(self):
        s = Solution.Solution()
        self.assertTrue(s.solve([10,5,6,1,2,3,4])) 

    def test_non_full_heap_even(self):
        s = Solution.Solution()
        self.assertTrue(s.solve([10,5,6,1,2,3,4,-1,-2]))     
    
    def test_non_full_heap_odd(self):
        s = Solution.Solution()
        self.assertTrue(s.solve([10,5,6,1,2,3,4,-1]))     

    def test_non_full_non_heap_odd(self):
        s = Solution.Solution()
        self.assertFalse(s.solve([10,5,6,1,2,3,4,3]))    

    def test_non_full_non_heap_even(self):
        s = Solution.Solution()
        self.assertFalse(s.solve([10,5,6,1,2,3,4,-1,5]))   

    def test_full_min_heap(self):
        s = Solution.Solution()
        self.assertFalse(s.solve([1,2,3])) 
