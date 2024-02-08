"""
27. Remove Element
https://leetcode.com/problems/remove-element/description/
"""

from typing import List


class Solution:
    """
    Time:   O(n)
    Space:  O(1)

    Two Pointers
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


class Solution:
    """
    Time:   O(n)
    Space:  O(1)

    Two Pointers
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0  # fast pointer
        slow = 0  # slow pointer
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


class Solution:
    """
    Time:   O(n)
    Space:  O(1)
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i-p] == val:
                nums.pop(i-p)
                p += 1
        return len(nums)
