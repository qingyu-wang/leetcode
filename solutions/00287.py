"""
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/description/
"""

from typing import List


class Solution:
    """
    Time:   O(n)
    Space:  O(n)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        cache = set()
        for i in nums:
            if i not in cache:
                cache.add(i)
            else:
                return i
        return


class Solution:
    """
    Time:   O(n)
    Space:  O(1)

    Count with index and negative value
    """
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]
        return len(nums)


class Solution:
    """
    Time:   O(n)
    Space:  O(1)

    Floyd's Cycle Detection
    https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode
    """
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
 
        # Find the meet point of 2 pointers
        # 
        # Use number in array as node and link
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find start of loop
        # p: the path from [start of array] to [start of loop]
        # x: the path from [meet point] to [start of loop]
        # c: the length of the loop
        #
        # 2 slow_path = fast_path
        # 2 (p+c-x+mc) = p+c-x+nc
        # 2p+2c-2x+2mc = p+c-x+nc
        # p = x + (n-1-2m)c
        #
        # which mean when pointers start from [start of array] and [meet point]
        # they will always meet at [start of loop]
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
