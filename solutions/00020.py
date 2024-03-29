"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
"""

class Solution:
    """
    Time:   O(n)
    Space:  O(n)
    """
    def isValid(self, s: str) -> bool:
        i_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        cache = []

        for i in s:
            if i not in i_map:
                cache.append(i)
            else:
                if not cache or i_map[i] != cache[-1]:
                    return False
                else:
                    cache.pop(-1)

        if not cache:
            return True
        else:
            return False
