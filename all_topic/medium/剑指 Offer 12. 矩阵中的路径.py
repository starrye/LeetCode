# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 12. 矩阵中的路径.py
@Author: liuwz
@time: 2022/1/10 10:23 上午
@desc: 
"""
from typing import List

"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 
例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。


 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
 

提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if self.dfs(board, rows, cols, word, row, col, 0):
                    return True
        return False

    def dfs(self, board, rows, cols, word, row, col, k):
        if row >= rows or row < 0 or col >= cols or col < 0 or board[row][col] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        board[row][col] = ''
        # result = False
        # for n_r, n_c in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
        #     result = self.dfs(board, rows, cols, word, n_r, n_c, k+1) or result
        result = self.dfs(board, rows, cols, word, row+1, col, k+1) or self.dfs(board, rows, cols, word, row-1, col, k+1) or self.dfs(board, rows, cols, word, row, col+1, k+1) or self.dfs(board, rows, cols, word, row, col-1, k+1)
        board[row][col] = word[k]
        return result


a = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCEDS")
print(a)