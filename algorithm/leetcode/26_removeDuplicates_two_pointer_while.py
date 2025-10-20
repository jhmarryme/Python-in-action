"""
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size
        slow, fast = 0, 1
        while fast < size:
            if nums[slow] != nums[fast]:
                slow+=1
                nums[slow] = nums[fast]
            fast+=1
        return slow + 1

nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
