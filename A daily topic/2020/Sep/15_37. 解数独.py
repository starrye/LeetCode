#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 37. 解数独.py
@time: 2020/9/15 09:29
@desc: 
"""
from functools import lru_cache
from typing import List
"""
编写一个程序，通过已填充的空格来解决数独问题。
一个数独的解法需遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。


一个数独。



答案被标成红色。

Note:
给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.flag = False
        rows = [[]*9 for _ in range(9)]
        cols = [[]*9 for _ in range(9)]
        squares = [[]*9 for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    rows[row].append(board[row][col])
                    cols[col].append(board[row][col])
                    squares[row // 3 * 3 + col // 3].append(board[row][col])

        def dfs(board, start_row, start_col, rows, cols, squares):
            for row in range(start_row, 9):
                for col in range(start_col, 9):
                    if board[row][col] == '.':
                        for i in range(1, 10):
                            i = str(i)
                            if i not in cols[col] and i not in rows[row] and i not in squares[row // 3 * 3 + col // 3]:
                                # 是时候做出选择了
                                cols[col].append(i)
                                rows[row].append(i)
                                squares[row // 3 * 3 + col // 3].append(i)
                                board[row][col] = i
                                # 进入递归
                                dfs(board, row, 0, rows, cols, squares)
                                # 满足条件 跳出去
                                if self.flag:
                                    return
                                # 撤销选择
                                board[row][col] = '.'
                                cols[col].remove(i)
                                rows[row].remove(i)
                                squares[row // 3 * 3 + col // 3].remove(i)
                        else:
                            return
                if row == 8 and col == 8:
                    self.flag = True
        dfs(board, 0, 0, rows, cols, squares)
        # print(board)


        print(board)
        # return board


a = Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
# print(a)