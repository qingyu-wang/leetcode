"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/description/
"""

class Solution:

    def isPalindrome(self, x: int) -> bool:
        """
        Time:  O(n)
        Space: O(1)
        """
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

    def isPalindrome(self, x: int) -> bool:
        """
        Time:  O(n)
        Space: O(n)
        """
        x_str = str(x)
        return x_str == x_str[::-1]
