class HashTable:
    """
       Goal is to implement simple hashtable with following operations:
        - put
        - get
        - remove
        The implementation here is based on hashing, having prime number of buckets
        and dynamically extending buckets up to next prime (up to 35797)
        Buckets hold lists to handle collisions

        Space complexity: O(|elements added|)
        Time complexity: O(1) amortized expected, O(n) worst case
    
    """
    primes = [7 , 89, 311, 827, 2003, 4621,	8821, 17713,  35797]
    def __init__(self):
        self.n = HashTable.primes[0]
        self.primeIdx = 1
        self.elements = [[] for _ in range(self.n)]
        self.currentCount = 0

    def extendAndRehash(self):
        self.n = HashTable.primes[self.primeIdx]
        self.primeIdx += 1
        extended = [[] for _ in range(self.n)]
        for bucket in self.elements:
            for item in bucket:
                extended[hash(item[0]) % self.n].append(item)
        self.elements = extended

    def put(self, key, val):
        if self.currentCount > self.n * 0.7 and self.primeIdx < len(HashTable.primes):
            self.extendAndRehash()
        idx = hash(key) % self.n
        bucket = self.elements[idx]
        for i in range(len(bucket)):
            (bkey, _) = bucket[i]
            if bkey == key:
                bucket[i] = (key, val)
                return
        
        self.currentCount += 1
        bucket.append((key, val)) 

    def get(self, key):
        idx = hash(key) % self.n
        bucket = self.elements[idx]
        for (bkey, val) in bucket:
            if bkey == key:
                return val
        return -1

    def remove(self, key):
        idx = hash(key) % self.n
        bucket = self.elements[idx]
        for i in range(len(bucket)):
            (bkey, _) = bucket[i]
            if bkey == key:
                del bucket[i]
                self.currentCount -= 1
                break