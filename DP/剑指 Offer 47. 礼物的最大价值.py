# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 47. 礼物的最大价值.py
@Author: liuwz
@time: 2022/1/5 10:47 上午
@desc: 
"""
from typing import List

"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200

"""


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 二维dp
        # rows, cols = len(grid), len(grid[0])
        # dp = grid
        # for i in range(rows):
        #     for j in range(cols):
        #         if i == 0 and j > 0:
        #             dp[i][j] += dp[i][j-1]
        #         elif i > 0 and j == 0:
        #             dp[i][j] += dp[i-1][j]
        #         elif i > 0 and j > 0:
        #             dp[i][j] += max(dp[i-1][j], dp[i][j-1])
        # return dp[-1][-1]

        # 二维简化判断dp
        # rows, cols = len(grid), len(grid[0])
        # dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        # for i in range(rows):
        #     for j in range(cols):
        #         dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # return dp[-2][-2]

        # 一维dp
        # rows, cols = len(grid), len(grid[0])
        # dp = [grid[0][0]] * cols
        # for i in range(rows):
        #     for j in range(cols):
        #         if i == 0 and j > 0:
        #             dp[j] = dp[j-1] + grid[i][j]
        #         elif i > 0 and j == 0:
        #             dp[j] = dp[j] + grid[i][j]
        #         elif i > 0 and j > 0:
        #             dp[j] = max(dp[j], dp[j-1]) + grid[i][j]
        # return dp[-1]

        # 一维简化判断dp
        rows, cols = len(grid), len(grid[0])
        dp = [grid[0][0]] * cols + [0]
        for i in range(rows):
            for j in range(cols):
                if i == j == 0:
                    continue
                dp[j] = max(dp[j], dp[j-1]) + grid[i][j]
        return dp[-2]
a = Solution().maxValue([[1,2,5],[3,2,1]])
print(a)