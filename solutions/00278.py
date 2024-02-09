"""
278. First Bad Version
https://leetcode.com/problems/first-bad-version/description/
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def isBadVersion():
    return 


class Solution:
    """
    time:   O(logn)
    space:  O(1)
    """
    def firstBadVersion(self, n: int) -> int:
        pl = 0
        pr = n - 1
        while pl <= pr:
            mid = (pl+pr)//2
            if isBadVersion(mid):
                pr = mid - 1
            else:
                pl = mid + 1
        return pl


class Solution:
    """
    time:   O(logn)
    space:  O(1)
    """
    def firstBadVersion(self, n: int) -> int:
        pl = 0
        pr = n - 1
        while pl <= pr:
            mid = (pl+pr)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1) or mid == 0:
                    return mid
                else:
                    pr = mid - 1
            else:
                    pl = mid + 1
        return pl
