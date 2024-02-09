"""
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/description/
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        pl = 0
        pr = row*col-1
        while pl <= pr:
            mid = (pl+pr)//2
            val = matrix[mid//col][mid%col]
            if val < target:
                pl = mid + 1
            elif val > target:
                pr = mid - 1
            else:
                return True
        return False
