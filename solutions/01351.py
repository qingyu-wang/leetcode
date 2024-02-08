"""
1351. Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
"""

from typing import List


class Solution:
    """
    Time:   O(m+n)
    Space:  O(1)
    """
    def countNegatives(self, grid):
        row_num = len(grid)
        col_num = len(grid[0])
        row_idx = row_num - 1
        col_idx = 0
        count = 0
        while row_idx >= 0 and col_idx < col_num:
            if grid[row_idx][col_idx] < 0:
                count += col_num - col_idx
                row_idx -= 1
            else:
                col_idx += 1
        return(count)


class Solution:
    """
    Time:   O(mlogn)
    Space:  O(1)
    """
    def countNegatives(self, grid: List[List[int]]) -> int:
        num = 0
        for arr in grid:
            pl = 0
            pr = len(arr) - 1
            while pl <= pr:
                mid = (pl+pr)//2
                if (mid == 0 or arr[mid-1]>=0) and arr[mid] < 0:
                    num += len(arr) - mid
                    break
                if arr[mid] < 0:
                    pr = mid - 1
                else:
                    pl = mid + 1
        return num
