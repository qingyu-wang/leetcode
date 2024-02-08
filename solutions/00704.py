"""
704. Binary Search
https://leetcode.com/problems/binary-search/description/
"""

from typing import List


class Solution:
    """
    Time:   O(logn)
    Space:  O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        idx_l = 0
        idx_r = len(nums)-1

        while idx_r >= idx_l:
            idx_m = idx_l + (idx_r-idx_l)//2
            if nums[idx_m] == target:
                return idx_m
            elif nums[idx_m] > target:
                idx_r = idx_m - 1
            else:
                idx_l = idx_m + 1

        return -1


class Solution:
    """
    Time:   O(log(n))
    Space:  O(log(n))

    Recursive
    """
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        idx_m = len(nums)//2
        if nums[idx_m] == target:
            return idx_m

        elif nums[idx_m] > target:
            idx = self.search(nums[:idx_m], target)
            if idx != -1:
                return idx

        else:
            idx = self.search(nums[idx_m+1:], target)
            if idx != -1:
                return idx+idx_m+1

        return -1
