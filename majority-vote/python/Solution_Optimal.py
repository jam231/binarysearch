class Solution:
    """
        We are given list of n integers and we need to either return an element
        whose frequency is higher than floor(n/2) or -1 if there is no such element.
        Additional constraint is that we can only use O(1) extra space.

        This solution is pretty much the entirety of Boyer Moore's Majority Voting algorithm.
        https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
        Main idea of that algorithm is that if there is a majority element, then it will cause
        > floor(n / 2) increases/decreases, and since there is less than half of other elements
        these elements don't have enough increases/decreases to counter the majority element, so 
        it will bubble up in the end.

        Time complexity: O(n)
        Space complexity: O(1)
    """
    def solve(self, nums):
        if not nums:
            return -1
        
        current, sighted = None, 0
        for n in nums:
            if sighted == 0:
                current, sighted = n, 1
            elif current != n:
                sighted -= 1
            else:
                sighted += 1
        
        if nums.count(current) > len(nums) // 2:
            return current
        return -1
        

