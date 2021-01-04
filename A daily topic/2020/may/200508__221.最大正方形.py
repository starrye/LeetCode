#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 221.最大正方形.py
@time: 2020/5/8 09:42
@desc: 
"""
from typing import List

"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 动态转移方程
        # 取决于三个位置只要有一个为0则当前位置为1
        # dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
        # 第一行与第一列上的数字如果为1 dp[i][j] = 1 也就是dp的出发点
        if not matrix or not matrix[0]:
            return 0
        maxside = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(dp[row-1][col],dp[row][col-1], dp[row-1][col-1]) + 1
                    maxside = max(maxside, dp[row][col])
        return maxside * maxside



a = Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
b = Solution().maximalSquare([])
c = Solution().maximalSquare([["1"],["1"],["1"]])
d = Solution().maximalSquare([["1","1","1"]])
e = Solution().maximalSquare([["0"]])
f = Solution().maximalSquare([["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]])
g = Solution().maximalSquare([["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]])
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)



