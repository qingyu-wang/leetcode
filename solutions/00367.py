"""
367. Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/description/
"""


class Solution:
    """
    Time:   O(logn)
    Space:  O(1)
    """
    def isPerfectSquare(self, num: int) -> bool:
        pl = 0
        pr = num
        while pl <= pr:
            mid = (pl+pr)//2
            if mid**2 < num:
                pl = mid + 1
            elif mid**2 > num:
                pr = mid - 1
            else:
                return True
        return False
