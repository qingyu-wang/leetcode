"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/description/
"""

from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Time:  O(logn)
        Space: O(1)
        """
        pl = 0
        pr = len(nums)-1

        while pl <= pr:
            mid = (pl+pr)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                pr = mid-1
            else:
                pl = mid+1

        # for the last situation
        # pl = pr
        # mid = (pl+pr)//2 = pl
        # if nums[pl] > target:
        #     pr = pl-1 # pl not change
        # else:
        #     pl = pl+1
        return pl
