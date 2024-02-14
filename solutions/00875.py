"""
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/description/

same as 1283
"""

from typing import List


class Solution:
    """
    Time:   O(nlogn)
    Space:  O(1)

    Binary Search
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            L->
            R
            1 [2] 3
        val 3 [2] 1

                  L
                <-R
            1 [2] 3
        val 3 [2] 1

              L
            <-R
            1 2 3
        val 3 2 1
        """
        L = 1
        R = max(piles)
        while L <= R:
            M = (L+R)//2
            val = 0
            for num in piles:
                val += num//M
                val += 1 if num%M != 0 else 0
            if val > h:
                L = M + 1
            elif val < h:
                R = M - 1
            else:
                R = M - 1
        return L