"""
744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
"""

from typing import List


class Solution:
    """
    Time:   O(logn)
    Space:  O(1)
    """
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        pl = 0
        pr = len(letters) - 1 
        while pl <= pr:
            mid = (pl+pr)//2
            if (mid == 0 or letters[mid-1] <= target) and letters[mid] > target:
                return letters[mid]
            if letters[mid] > target:
                pr = mid - 1
            else:
                pl = mid + 1
        return letters[0]
