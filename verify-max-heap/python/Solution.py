class Solution:
    """
        [Easy] Verify Max Heap solution from binarysearch.com
        Problem is about verifying input list represents max heap, that is 
        for each i:
                nums[i] >= nums[2 * i + 1] 
            and
                nums[i] >= nums[2 * i + 1]
        Time complexity: O(n)
        Space complexity: O(1)
    """
    def solve(self, nums) -> bool:
        for i in range(len(nums)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(nums) and nums[i] < nums[left]:
                return False
            if right < len(nums) and nums[i] < nums[right]:
                return False
            # early break
            if right >= len(nums):
                break
        return True