import unittest
import Solution

class HashTableTests(unittest.TestCase):
    def test_put_get_remove_get(self):
        htable = Solution.HashTable()

        htable.put("aaaa aa", 103)
        self.assertEqual(htable.get("aaaa aa"), 103)
        htable.remove("aaaa aa")
        self.assertEqual(htable.get("aaaa aa"), -1)

    def test_put_put_get_remove_get(self):
        htable = Solution.HashTable()

        htable.put("aaaa aa", 103)
        htable.put("aaaa aa", 106)
        self.assertEqual(htable.get("aaaa aa"), 106)
        htable.remove("aaaa aa")
        self.assertEqual(htable.get("aaaa aa"), -1)


    def test_large(self):
        htable = Solution.HashTable()

        for i in range(100000):
            htable.put(i, str(i))
        for i in range(100000):
            self.assertEqual(htable.get(i), str(i))
        for i in range(100000):
            htable.remove(i)
            self.assertEqual(htable.get(i), -1)
