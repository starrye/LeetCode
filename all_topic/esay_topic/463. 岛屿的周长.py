#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 463. 岛屿的周长.py
@time: 2020/10/30 16:43
@desc: 
"""
from typing import List
"""
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

 

示例 :

输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

输出: 16

解释: 它的周长是下面图片中的 16 个黄色的边：
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        one_list = []
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    one_list.append([row, col])
        for row_, col_ in one_list:
            around_one = 0
            for dx, dy in [[1,0],[-1,0],[0,-1],[0,1]]:
                if 0 <= row_ + dx < len(grid) and 0 <= col_ + dy < len(grid[0]) and grid[row_ + dx][col_ + dy] == 1:
                    around_one += 1
            result_dict = {0:4, 1:3, 2:2, 3:1, 4:0}
            result += result_dict[around_one]
        return result