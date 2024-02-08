"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/description/
"""

from typing import List


class Solution:
    """
    Compare between the minimum and maximum

    Time:   O(n)
    Space:  O(n)
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        res = [None] * len(nums)
        while k >= 0:
            if nums[i]**2 > nums[j]**2:
                res[k] = nums[i]**2
                i += 1
                k -= 1
            else:
                res[k] = nums[j]**2
                j -= 1
                k -= 1
        return res
