"""
611. Valid Triangle Number
https://leetcode.com/problems/valid-triangle-number/description/
"""

from typing import List


class Solution:
    """
    Time:   O(n^2logn+nlogn)
    Space:  O(1)

    Two Pointers
    """
    def triangleNumber(self, nums: List[int]) -> int:
        cnt = 0
        nums = sorted(nums) # Time Complexity O(nlogn)
        for i in range(len(nums)-1, -1, -1):
            T = nums[i]
            L = 0
            R = i - 1
            while R > L:
                if nums[L] + nums[R] > T:
                    out += R - L
                    R -= 1
                else:
                    L += 1
        return cnt


class Solution:
    """
    Time:   O(n^2logn+nlogn)
    Space:  O(1)

    Binary Search
    """
    def triangleNumber(self, nums: List[int]) -> int:
        """
        L+1
        M
        R
        1 2 3     2

          L
          M
          R-1
        1 2 3

            L
            M
            R-1
        1 2 3     2
        """
        def bs(nums, s):
            l = len(nums)
            L = s
            R = l-1
            while L <= R:
                M = (L+R)//2
                T = nums[i]+nums[j]
                V = nums[M]
                if V < T:
                    L = M+1
                elif V > T:
                    R = M-1
                else:
                    R = M-1
            return R-s+1 if R >= s else 0

        cnt = 0
        nums.sort() # Time Complexity O(nlogn)
        l = len(nums)
        for i in range(0,l-2):
            for j in range(i+1,l-1):
                cnt += bs(nums, j+1)
        return cnt
