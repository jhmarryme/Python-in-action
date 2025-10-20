"""
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow+=1
                nums[slow] = nums[fast]

        return slow
nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
