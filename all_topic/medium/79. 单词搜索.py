#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 79. 单词搜索.py
@time: 2020/9/29 16:59
@desc: 
"""
from typing import List
"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        use_location = set()
        def dfs(row, col, word):
            if not len(word):
                return True
            flag = False
            if board[row][col] == word[0]:
                if len(word) == 1:
                    return True
                # nonlocal use_location
                use_location.add((row, col))
                for d_row, d_col in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_row, new_col = row+d_row, col+d_col
                    if rows > new_row >= 0 and cols > new_col >= 0 and (new_row, new_col) not in use_location:
                        flag = flag or dfs(new_row, new_col, word[1:])
                use_location.remove((row, col))
            return flag
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, word):
                    return True
        return False



a = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")
print(a)





