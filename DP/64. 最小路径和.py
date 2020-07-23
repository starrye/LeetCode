#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 64. 最小路径和.py
@time: 2020/7/23 09:54
@desc: 
"""
from typing import List
"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # dp = [[grid[0][0] for _ in range(n)] for _ in range(m)]
        # print(dp)
        # for i in range(0,m):
        #     for j in range(0, n):
        #         if i == 0 and j == 0:
        #             continue
        #         if i == 0:
        #             dp[i][j] = dp[i][j-1] + grid[i][j]
        #         elif j == 0:
        #             dp[i][j] = dp[i-1][j] + grid[i][j]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # return dp[-1][-1]

        dp = [grid[0][0] for _ in range(n)]
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]


a = Solution().minPathSum([[1,3,1],[1,5,1]])
print(a)