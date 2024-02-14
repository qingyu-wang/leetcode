"""
1283. Find the Smallest Divisor Given a Threshold
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

same as 875
"""

from typing import List


class Solution:
    """
    Time:   O(nlogn)
    Space:  O(1)

    Binary Search
    """
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
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
        R = max(nums)
        while L <= R:
            M = (L+R)//2
            val = 0
            for num in nums:
                val += num//M
                val += 1 if num%M != 0 else 0
            if val > threshold:
                L = M + 1
            elif val < threshold:
                R = M - 1
            else:
                R = M - 1
        return L
