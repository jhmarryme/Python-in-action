from typing import List

"""
https://leetcode.cn/problems/remove-element/description/
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len([x for x in nums if x == val])
        for _ in range(size):
            nums.remove(val)
            nums.append(0)
        return len(nums) - size


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution().removeElement(nums, val))
