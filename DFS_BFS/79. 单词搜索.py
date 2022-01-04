#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 79. 单词搜索.py
@time: 2020/9/29 16:59
@desc: 
"""
from collections import deque
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
        begin_point = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    begin_point.append([i, j])

        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for b_row, b_col in begin_point:
            queue_ = deque()
            used = set()
            used.add((b_row, b_col))
            word_index = 1
            queue_.append([b_row, b_col])

            while queue_:
                flag = False
                if word_index == len(word):
                    return True
                row, col = queue_.popleft()
                for drow, dcol in direction:
                    nrow, ncol = row + drow, col + dcol

                    if 0 <= nrow < rows and 0 <= ncol < cols and (nrow, ncol) not in used:
                        if board[nrow][ncol] == word[word_index]:
                            flag = True
                            if word_index == len(word):
                                return True
                            used.add((nrow, ncol))
                            queue_.append([nrow, ncol])
                if flag:
                    word_index += 1
        return False



a = Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]]
, "AAB")
print(a)





