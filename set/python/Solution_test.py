import unittest
import Solution

class SetTests(unittest.TestCase):
    def test_large(self):
        customSet = Solution.CustomSet()
        for i in range(100000):
            customSet.add(i)
        for i in range(100000):
            self.assertTrue(customSet.exists(i))
        for i in range(100000):
            customSet.remove(i)
            self.assertFalse(customSet.exists(i))

    def test_small(self):
        customSet = Solution.CustomSet()
        s1 = "lal fdslafd fsdfsfsdfs f"
        s2 = "fd fsdf fsdf"
        customSet.add(s1)
        self.assertTrue(customSet.exists(s1))
        self.assertFalse(customSet.exists(s2))
        customSet.remove(s1)
        self.assertFalse(customSet.exists(s1))
        self.assertFalse(customSet.exists(s2))
