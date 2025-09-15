class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]
        max_sum = nums[0]
        for i in range(0, len(nums)):
            sum = nums[i]
            max_sum = max(max_sum, sum)
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                max_sum = max(max_sum, sum)
        return max_sum
