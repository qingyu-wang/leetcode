"""
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""

from typing import List


class Solution:
    """
    Time:   O(logn)
    Space:  O(1)
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(x):
            """
            find the right side value next to the largest value less than x
            """
            pl = 0
            pr = len(nums)
            # pr = len(nums) - 1
            while pl < pr:
            # while pl <= pr:
                mid = (pl+pr)//2
                if nums[mid] < x:
                    pl = mid+1
                else:
                    pr = mid
                    # pr = mid-1
            return pl

        ps = search(target)
        pe = search(target+1)-1

        if ps <= pe:
            return [ps, pe]

        return [-1, -1]


class Solution:
    """
    Time:   O(logn)
    Space:  O(1)
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pl = 0
        pr = len(nums) - 1
        while pl <= pr:
            # pl mid pr
            mid = (pl+pr)//2

            if target == nums[mid]:

                prl = mid
                while prl < pr:
                    # mid/prl midr pr
                    midr = (prl+pr)//2
                    if target == nums[midr]:
                        if target != nums[midr+1]:
                            pr = midr
                            break
                        else:
                            prl = midr + 1
                    else:
                        # target > nums[midr]
                        pr = midr - 1

                plr = mid
                while pl < plr:
                    # pl midl plr/mid
                    midl = (pl+plr)//2
                    if target == nums[midl]:
                        if midl == 0 or target != nums[midl-1]:
                            pl = midl
                            break
                        else:
                            plr = midl - 1
                    else:
                        # target < nums[midl]
                        pl = midl + 1

                return [pl, pr]

            if target > nums[mid]:
                pl = mid + 1
            else:
                pr = mid - 1

        return [-1, -1]
