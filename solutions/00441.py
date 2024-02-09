"""
441. Arranging Coins
https://leetcode.com/problems/arranging-coins/description/
"""

class Solution:
    """
    Time:   O(logn)
    Space:  O(1)

    pl = 0
    pr = n
    while pl <= pr:
        mid = (pl+pr)//2
        if mid < target:
            pl = mid + 1
        elif mid > target:
            pr = mid - 1
        else:
            [analysis]
    """
    def arrangeCoins(self, n: int) -> int:
        pl = 1
        pr = n
        while pl <= pr:
            mid = (pl+pr)//2
            if (1+mid)*mid//2 < n:
                pl = mid + 1
            elif (1+mid)*mid//2 > n:
                pr = mid - 1
            else:
                return mid
        return pr
