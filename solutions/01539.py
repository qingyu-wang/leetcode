"""
1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/description/
"""

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
           L
           M
         <-R
        [2,5,8] 2
        [1,3,5]
         1 3 6 9
           4 7 10

             L->
             M
             R
        [2,5,8] 6
        [1,3,5]
         1 3 6 9
           4 7 10

         L
         M
       <-R
        [2,5,8] 1
        [1,3,5]
         1 3 6 9
           4 7 10

        val = arr[pl] - 1 - (miss - k + 1)
        val = arr[pl] - 1 - ((arr[pl] - pl - 1) - k)
        val = arr[pl] - 1 - arr[pl] + pl + 1 + k
        val = pl + k
        """
        pl = 0
        pr = len(arr)-1
        while pl <= pr:
            mid = (pl+pr)//2
            miss = arr[mid] - mid - 1
            if miss < k:
                pl = mid + 1
            elif miss > k:
                pr = mid - 1
            else:
                pr = mid - 1
        return pl + k
