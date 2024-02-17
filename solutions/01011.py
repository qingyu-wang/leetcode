"""
1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
"""

from typing import List


class Solution:
    """
    Time:   O(?)
    Space:  O(?)

    Binary Search

      [L]->
       R
    w: 1 [2] 3
    d: 3 [2] 1

            [L]
           <-R
    w: 1 [2] 3
    d: 3 [2] 1

        [L]
       <-R
    w: 1 2 3
    d: 3 2 1
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L = max(weights)
        R = len(weights)*500
        while L <= R:
            M = (L+R)//2
            day = 0
            wgt = 0
            for w in weights:
                wgt += w
                if wgt > M:
                    wgt = w
                    day += 1
                if wgt > M:
                    wgt = 0
                    day += 1
            if wgt != 0:
                day += 1
            if day < days:
                R = M-1
            elif day > days:
                L = M+1
            else:
                R = M-1
        return L
