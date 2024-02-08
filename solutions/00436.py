"""
436. Find Right Interval
https://leetcode.com/problems/find-right-interval/description/
"""

from typing import List


class Solution:
    """
    Time:   O(nlogn)
    Space:  O(n)
    """
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        maps_s = {}
        nums_s = []
        nums_e = []
        for j, (s, e) in enumerate(intervals):
            maps_s[s] = j
            nums_s.append(s)
            nums_e.append(e)
        nums_s.sort()

        rets = []
        for i, e in enumerate(nums_e):
            ret = -1
            pl = 0
            pr = len(nums_s)
            # pr = len(nums_s) - 1
            while pl < pr:
            # while pl <= pr:
                mid = (pl+pr)//2
                s = nums_s[mid]
                if s >= e:
                    if ret == -1:
                        min_old = s - e
                        ret = maps_s[s]
                    else:
                        min_new = s - e
                        if min_new < min_old:
                            min_old = min_new
                            ret = maps_s[s]
                    pr = mid
                    # pr = mid - 1
                else:
                    pl = mid + 1
            rets.append(ret)

        return rets


class Solution:
    """
    Time:   O(n^2)
    Space:  O(n)
    """
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        nums_s = []
        nums_e = []
        for s, e in intervals:
            nums_s.append(s)
            nums_e.append(e)

        rets = []
        for i, e in enumerate(nums_e):
            ret = -1
            for j, s in enumerate(nums_s):
                if s >= e:
                    if ret == -1:
                        min_old = s - e
                        ret = j
                    else:
                        min_new = s - e
                        if min_new < min_old:
                            min_old = min_new
                            ret = j
            rets.append(ret)

        return rets
