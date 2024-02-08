"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/description/
"""

class Solution:
    """
    Time:   O(n)
    Space:  O(1)
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        x_len = len(x_str)
        ps = 0
        pe = x_len-1
        for i in range(x_len//2):
            if x_str[ps] != x_str[pe]:
                return False
            ps += 1
            pe -= 1
        return True


class Solution:
    """
    Time:   O(n)
    Space:  O(n)
    """
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]
