class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums)
        
        ans = min(
            nums[n-1] - nums[3],  # Scenario 1: remove 3 largest
            nums[n-2] - nums[2],  # Scenario 2: remove 2 largest, 1 smallest
            nums[n-3] - nums[1],  # Scenario 3: remove 1 largest, 2 smallest
            nums[n-4] - nums[0]   # Scenario 4: remove 3 smallest
        )
        
        return ans
