#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 861. 翻转矩阵后的得分.py
@time: 2020/7/27 16:59
@desc: 
"""
from typing import List
"""
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
返回尽可能高的分数。

 

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1
"""


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        from collections import Counter
        rows = len(A)
        cols = len(A[0])
        for row in range(rows):
            if A[row][0] == 0:
                for col in range(cols):
                    A[row][col] = 1 if not A[row][col] else 0
        A_ = zip(*A)
        res = 0
        for i in A_:
            cols -= 1
            dic = Counter(i)
            res += max(dic[0], dic[1]) * 2 ** cols
        return res



a = Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
print(a)

