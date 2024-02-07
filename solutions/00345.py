"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/description/
"""

class Solution:

    def reverseVowels(self, s: str) -> str:
        """
        Time:  O(n)
        Space: O(1)

        Time: n
        2 pointers
        """
        s = list(s)
        ps = 0
        pe = len(s)-1
        while ps < pe:
            while ps < pe and s[ps].lower() not in "aeiou":
                ps += 1
            while ps < pe and s[pe].lower() not in "aeiou":
                pe -= 1
            if ps < pe and s[ps].lower() in "aeiou" and s[pe].lower() in "aeiou":
                s[ps],s[pe]=s[pe],s[ps]
                ps += 1
                pe -= 1
        s = "".join(s)
        return s

    def reverseVowels(self, s: str) -> str:
        """
        Time:  O(n)
        Space: O(1)

        Time: 2n
        """
        cache = ""
        for i in s:
            if i.lower() in "aeiou":
                cache += i
        out = ""
        cache_idx = len(cache)-1
        for i in s:
            if i.lower() in "aeiou":
                out += cache[cache_idx]
                cache_idx -= 1
            else:
                out += i
        return out
