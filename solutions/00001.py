"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/
"""

from typing import List


class Solution:
    """
    Time:   O(n)
    Space:  O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx, num in enumerate(nums):
            sub = target - num
            if sub in num_map:
                return [num_map[sub], idx]
            else:
                num_map[num] = idx
        return None
