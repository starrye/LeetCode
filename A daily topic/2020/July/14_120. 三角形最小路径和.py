#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 120. 三角形最小路径和.py
@time: 2020/7/14 09:56
@desc: 
"""
from typing import List
"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点
例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
 
说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp n2
        # 动态转移方程
        # dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])
        # 注意初始值

        # 从上到下
        # if len(triangle) == 0:
        #     return 0
        # if len(triangle) == 1:
        #     return triangle[0][0]
        # for i in range(1, len(triangle)):
        #     for j in range(len(triangle[i])):
        #         if j == 0:
        #             triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
        #         elif j == len(triangle[i]) - 1:
        #             triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
        #         else:
        #             triangle[i][j] = min(triangle[i - 1][j], triangle[i - 1][j - 1]) + triangle[i][j]
        # return min(triangle[-1])

        # 从下到上
        for i in range(len(triangle)-1, 0, -1):
            for j in range(i):
                triangle[i-1][j] += min(triangle[i][j], triangle[i][j+1])
        return triangle[0][0]

a = Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(a)


