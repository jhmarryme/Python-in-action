"""
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = [nums[i] for i in range(1, len(nums)) if nums[i] == nums[i - 1]]
        for v in duplicates:
            nums.remove(v)
            nums.append(v)
        return len(nums) - len(duplicates)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
