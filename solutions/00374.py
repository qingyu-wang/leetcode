"""
374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/description/
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return


class Solution:
    """
    Time:   O(logn)
    Space:  O(1)
    """
    def guessNumber(self, n: int) -> int:
        pl = 1
        pr = n
        while pl <= pr:
            mid = (pl+pr)//2
            if guess(mid) == -1:
                pr = mid - 1
            elif guess(mid) == 1:
                pl = mid + 1
            else:
                return mid
        return
