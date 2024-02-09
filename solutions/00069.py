"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/description/
"""

class Solution:
    """
    Time:   O(logn)
    Space:  O(1)
    """
    def mySqrt(self, x: int) -> int:
        pl = 0
        pr = x
        while pl <= pr:
            mid = (pl+pr)//2
            if mid**2 < x:
                pl = mid + 1
            elif mid**2 > x:
                pr = mid - 1
            else:
                pl = mid + 1
        return pr
