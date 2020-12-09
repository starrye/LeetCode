#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 62. 不同路径.py
@time: 2020/12/9 09:33
@desc:
"""
from typing import List
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？

 

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 二维dp
        # dp = [[1] * n for _ in range(m)]
        # for rows in range(m):
        #     for cols in range(n):
        #         if rows > 0 and cols > 0:
        #             dp[rows][cols] = dp[rows-1][cols]+dp[rows][cols-1]
        # return dp[-1][-1]

        # 一维dp
        dp = [1] * n
        for row in range(1, m):
            for col in range(1, n):
                dp[col] = dp[col-1] + dp[col]
        return dp[-1]

a = Solution().uniquePaths(7, 3)
print(a)