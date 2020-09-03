#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 51. N 皇后.py
@time: 2020/9/3 09:27
@desc: 
"""
from typing import List
"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
上图为 8 皇后问题的一种解法。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例：
输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
 
提示：
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        res = [["."] * n for _ in range(n)]
        # 列
        cols = [True] * n
        # 正对角线
        dg = [True] * (2 * n - 1)
        # 反对角线
        udg = [True] * (2 * n - 1)
        def dfs(row):
            tmp_ans = []
            # 当row == n时 每行都已经填上了Q
            if row == n:
                for i in range(n):
                    tmp_ans.append("".join(res[i]))
                ans.append(tmp_ans)
                return
            for col in range(n):
                if cols[col] and dg[n - 1 + row - col] and udg[row + col]:
                    res[row][col] = 'Q'
                    cols[col] = dg[n - 1 + row - col] = udg[row + col] = False
                    # 下一行
                    dfs(row + 1)
                    # 撤回
                    res[row][col] = "."
                    cols[col] = dg[n - 1 + row - col] = udg[row + col] = True

        dfs(0)
        return ans


a = Solution().solveNQueens(4)
print(a)