from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left


nums = [3, 2, 2, 3]
val = 3
print(Solution().removeElement(nums, val))
