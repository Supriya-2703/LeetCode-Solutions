class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current = 0

        for num in nums:
            # If current sum becomes negative, reset it
            if current < 0:
                current = 0
            
            current += num
            max_sum = max(max_sum, current)
        
        return max_sum
