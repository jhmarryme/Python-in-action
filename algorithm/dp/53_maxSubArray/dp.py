class Solution(object):
    def maxSubArray(self, nums):
        """
        https://leetcode.cn/problems/maximum-subarray/solutions/9058/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai
        时间复杂度：O(N)
        空间复杂度：O(N)
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max((dp[i - 1] + nums[i]), nums[i])
        return max(dp)
