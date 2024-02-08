"""
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""

from typing import List


class Solution:
    """
    Time:   O(n)
    Space:  O(1)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        arr = nums
        point_l = 0
        point_r = 0
        sub_arr_sum = 0
        sub_arr_len_min = 0

        for point_r in range(len(arr)):
            sub_arr_sum += arr[point_r]
            if sub_arr_sum >= target:
                while sub_arr_sum - arr[point_l] >= target:
                    sub_arr_sum -= arr[point_l]
                    point_l += 1
                sub_arr_len = point_r - point_l + 1
                if sub_arr_len_min == 0 or sub_arr_len_min > sub_arr_len:
                    sub_arr_len_min = sub_arr_len
        return sub_arr_len_min


class Solution:
    """
    Time:   O(n)
    Space:  O(n)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        arr = nums
        sub_arr = []
        sub_arr_sum = 0
        sub_arr_len = 0
        for i in arr:
            sub_arr.append(i)
            sub_arr_sum += i
            while sub_arr_sum - sub_arr[0] >= target:
                sub_arr_sum -= sub_arr[0]
                sub_arr.pop(0)
            if sub_arr_sum >= target:
                if sub_arr_len == 0 or sub_arr_len > len(sub_arr):
                    sub_arr_len = len(sub_arr)
        return sub_arr_len
