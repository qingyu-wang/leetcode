"""
59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/description/
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(n)]
        i = 0
        j = 0
        i_limit = [1, n-1]
        j_limit = [0, n-1]
        move = "j"
        mode = "+"
        for k in range(1, n*n+1):
            matrix[i][j] = k
            if move == "j":
                if mode == "+":
                    if j < j_limit[1]:
                        j += 1
                    else:
                        j_limit[1] -= 1
                        move = "i"
                        i += 1
                else:
                    if j > j_limit[0]:
                        j -= 1
                    else:
                        j_limit[0] += 1
                        move = "i"
                        i -= 1
            else:
                if mode == "+":
                    if i < i_limit[1]:
                        i += 1
                    else:
                        i_limit[1] -= 1
                        mode = "-"
                        move = "j"
                        j -= 1
                else:
                    if i > i_limit[0]:
                        i -= 1
                    else:
                        i_limit[0] += 1
                        mode = "+"
                        move = "j"
                        j += 1
        return matrix
