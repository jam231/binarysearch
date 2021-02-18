class CustomSet:
    primes = [7 , 89, 311, 827, 2003, 4621,	8821, 17713,  35797]
    def __init__(self):  
        self.n = CustomSet.primes[0]
        self.primeIdx = 1
        self.internalList = [[] for _ in range(self.n)]
        self.elements = 0

    def extendAndRehash(self):
        self.n = CustomSet.primes[self.primeIdx]
        self.primeIdx += 1
        extended = [[] for _ in range(self.n)]
        for bucket in self.internalList:
            for item in bucket:
                extended[hash(item) % self.n].append(item)
        self.internalList = extended

    def add(self, val):
        if self.elements > self.n * 0.7 and self.primeIdx < len(CustomSet.primes):
            self.extendAndRehash()

        idx = hash(val) % self.n
        self.elements += 1
        
        bucket = self.internalList[idx]
        if val not in bucket:
            bucket.append(val)

    def exists(self, val):
        idx = hash(val) % self.n
        return val in self.internalList[idx]

    def remove(self, val):
        idx = hash(val) % self.n
        bucket = self.internalList[idx]
        for i in range(len(bucket)):
            if bucket[i] == val:
                del bucket[i]
                self.elements -= 1
                break