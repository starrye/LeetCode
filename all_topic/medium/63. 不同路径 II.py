#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 63. 不同路径 II.py
@time: 2020/7/6 09:19
@desc: 
"""
from typing import List
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
说明：m 和 n 的值均不超过 100。
示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]:
        #     return 0
        # rows = len(obstacleGrid)
        # cols = len(obstacleGrid[0])
        # dp = [[0] * cols for _ in range(rows)]
        # # 首位置
        # dp[0][0] = 1
        # for i in range(1, cols):
        #     if not obstacleGrid[0][i]:
        #         dp[0][i] = 1
        #     else:
        #         break
        # for j in range(1, rows):
        #     if not obstacleGrid[j][0]:
        #         dp[j][0] = 1
        #     else:
        #         break
        # for row in range(1, rows):
        #     for col in range(1, cols):
        #         if not obstacleGrid[row][col]:
        #             dp[row][col] = dp[row-1][col] + dp[row][col-1]
        # return dp[-1][-1]

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1] + [0] * n
        for i in range(0, m):
            for j in range(0, n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
        return dp[-2]

a = Solution().uniquePathsWithObstacles([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
print(a)

