#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 542.01矩阵.py
@time: 2020/4/15 13:53
@desc: 
"""
"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。
示例 1: 
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2: 
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
"""


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # BFS
        # 先获取多个0点
        # 从0点出发四周扩散 犹如 下雨到一片湖起的涟漪 重点是防止重复处理
        # 0到 非0点的距离
        from collections import deque
        queue_ = deque()
        res = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for rows in range(len(matrix)):
            for cols in range(len(matrix[0])):
                if matrix[rows][cols] == 0:
                    res[rows][cols] = 0
                    queue_.append([rows, cols])
        while queue_:
            x, y = queue_.popleft()
            for x_offset, y_offset in [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]:
                if 0 <= x_offset < len(matrix) and 0 <= y_offset < len(matrix[0]) and res[x_offset][y_offset] == -1:
                    res[x_offset][y_offset] = res[x][y] + 1
                    queue_.append([x_offset, y_offset])
        return res


a = Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
print(a)
