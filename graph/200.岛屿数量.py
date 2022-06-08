# encoding: utf-8
"""
@Project ： 
@File: 200.岛屿数量.py
@Author: liuwz
@time: 2022/6/2 11:26 AM
@desc: 
"""
from collections import deque

import pandas as pd
import numpy as np
from typing import List

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        queue = deque()

        def bfs(row, col):
            dir = [[0,1], [0, -1], [1, 0], [-1, 0]]
            queue.append((row, col))
            while queue:
                x, y = queue.popleft()
                for dx, dy in dir:
                    if 0 <= x + dx < rows and 0 <= y + dy < cols and grid[x+dx][y+dy] == "1":
                        queue.append([x+dx,y+dy])
                        grid[x + dx][y + dy] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    print(grid)
                    ans += 1
        return ans


a = Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])