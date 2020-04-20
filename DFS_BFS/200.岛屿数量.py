#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 200.岛屿数量_200420.py
@time: 2020/4/20 08:59
@desc: 
"""
"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # BFS
        # res = 0
        # from collections import deque
        # queue_ = deque()
        # def bfs(x, y):
        #     grid[x][y] = "0"
        #     while queue_:
        #         x, y = queue_.popleft()
        #         for x_offset, y_offset in [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]:
        #             if 0 <= x_offset < len(grid) and 0 <= y_offset < len(grid[0]) and grid[x_offset][y_offset] == "1":
        #                 queue_.append([x_offset, y_offset])
        #                 grid[x_offset][y_offset] = "0"
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == "1":
        #             queue_.append((row, col))
        #             bfs(row, col)
        #             res += 1
        # return res
        # DFS
        res = 0
        def dfs(x, y):
            grid[x][y] = "0"
            for x_offset, y_offset in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0 <= x_offset < len(grid) and 0 <= y_offset < len(grid[0]) and grid[x_offset][y_offset] == "1":
                    dfs(x_offset, y_offset)
                    grid[x_offset][y_offset] = "0"
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1
        return res


a = Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(a)
