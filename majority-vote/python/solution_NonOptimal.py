class Solution:
    """
        We are given list of n integers and we need to either return an element
        whose frequency is higher than floor(n/2) or -1 if there is no such element.
        Additional constraint is that we can only use O(1) extra space.

        Simplest solution is to sort nums first, count consecutive elements, if we find one
        that has count higher than floor(n/2) we return it.

        Time complexity: O(nlogn)
        Space complexity: O(1) since we store only current element, and how many times 
        current element was seen
    """
    def solve(self, nums):
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        
        threshold = len(nums) / 2
        howMany = 0
        last = nums[0]
        for n in sorted(nums):
            if last == n:
                howMany += 1
            else:
                last = n
                howMany = 1
            
            if howMany > threshold:
                return n
        return -1