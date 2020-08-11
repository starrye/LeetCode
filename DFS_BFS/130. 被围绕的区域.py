#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 130. 被围绕的区域.py
@time: 2020/8/11 11:05
@desc: 
"""
from collections import deque
from typing import List
"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows == 0: return board
        cols = len(board[0])
        if cols == 0: return board
        border_zero = set()
        border_zero_queue = deque()
        inside_zero = set()
        
        # 边界 "O" 加入 border_zero_queue
        # 内部 "O" 加入 inside_zero
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                        border_zero_queue.append([row, col])
                    else:
                        inside_zero.add((row, col))

        # 边界 "O" 相连的 "O" 同样加入border_zero_queue，
        # 这一步主要是把所有可修改的"O"位置找出来(把边界 "O" 相连的 "O"从inside_zero中除去)
        while border_zero_queue:
            x, y = border_zero_queue.popleft()
            border_zero.add((x, y))
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x + dx < rows and 0 <= y + dy < cols and board[x+dx][y+dy] == "O" and (x+dx, y+dy) not in border_zero:
                    border_zero_queue.append([x+dx, y+dy])
                    if (x+dx, y+dy) in inside_zero:
                        inside_zero.remove((x+dx, y+dy))

        # 此时inside_zero中全部都是可修改的
        while inside_zero:
            x, y = inside_zero.pop()
            board[x][y] = "X"



# a = Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# b = Solution().solve([["X","X","X"],["X","O","X"],["X","X","X"]])
c = Solution().solve([["X","O","X"],["X","O","X"],["X","O","X"]])
# d = Solution().solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])
# print(a)
# print(b)
print(c)
# print(d)