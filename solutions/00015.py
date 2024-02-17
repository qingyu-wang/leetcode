"""
15. 3Sum
https://leetcode.com/problems/3sum/description/
"""

from typing import List


class Solution:
    """
    Time:   O(n)
    Space:  O(n)

    Two Pointer
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rets = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, rets)
        return rets

    def twoSum(self, nums: List[int], i: int, rets: List[List[int]]) -> None:
        slow = i+1
        fast = len(nums)-1
        while slow < fast:
            sum_ = nums[i] + nums[slow] + nums[fast]
            if sum_ < 0:
                slow += 1
            elif sum_ > 0:
                fast -= 1
            else:
                rets.append([nums[i], nums[slow], nums[fast]])
                slow += 1
                fast -= 1
                while slow < fast and nums[slow-1] == nums[slow]:
                    slow += 1
                while fast > slow and nums[fast+1] == nums[fast]:
                    fast -= 1
        return


class Solution:
    """
    Time:   O(n)
    Space:  O(n)

    Two Pointer
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        rets = list()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i != 0 and nums[i-1] == nums[i]:
                continue
            slow = i+1
            fast = l-1
            while slow < fast:
                sum_ = nums[i] + nums[slow] + nums[fast]
                if sum_ < 0:
                    slow += 1
                elif sum_ > 0:
                    fast -= 1
                else:
                    rets.append([nums[i], nums[slow], nums[fast]])
                    slow += 1
                    fast -= 1
                    while slow < fast and nums[slow-1] == nums[slow]:
                        slow += 1
                    while fast > slow and nums[fast+1] == nums[fast]:
                        fast -= 1
        return rets


class Solution:
    """
    Time:   O(n^2)
    Space:  O(n)

    Hash Table
    Exceed Time
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        rets = list()
        for i in range(0, l-2):
            val1 = nums[i]
            tgt = 0 - val1
            rem_map = dict()
            for j in range(i+1, l):
                val2 = nums[j]
                rem = tgt - val2
                if val2 in rem_map:
                    val3 = rem_map[val2]
                    ret = [val1, val2, val3]
                    if ret not in rets:
                        rets.append(ret)
                else:
                    rem_map[rem] = val2
        return rets
