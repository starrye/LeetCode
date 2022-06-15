# encoding: utf-8
"""
@Project ： 
@File: 498. 对角线遍历.py
@Author: liuwz
@time: 2022/6/14 10:32 AM
@desc: 
"""

import pandas as pd
import numpy as np
from typing import List

"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

 

示例 1：


输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]
示例 2：

输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # flag = -1
        # ans = []
        # m, n = len(mat) - 1, len(mat[0]) - 1
        # rc_sum = m + n
        # for line in range(rc_sum + 1):
        #     temp = []
        #     begin = max(line - n, 0)
        #     end = min(line + 1, m + 1)
        #     for i in range(begin, end):
        #         temp.append(mat[i][line-i])
        #     ans.extend(temp[::flag])
        #     flag = -flag
        # return ans

        ans, m, n, flag = [], len(mat) - 1, len(mat[0]) - 1, -1
        for line in range(m + n + 1):
            ans.extend([mat[i][line - i] for i in range(max(line - n, 0), min(line + 1, m + 1))][::flag])
            flag = -flag
        return ans

        # m, n, ans = len(mat), len(mat[0]), []
        # for k in range(m + n - 1):
        #     if not k % 2:
        #         ans += [mat[x][k - x] for x in range(min(m - 1, k), max(-1, k - n), -1)]
        #     else:
        #         ans += [mat[x][k - x] for x in range(max(0, k - n + 1), min(k + 1, m))]
        # return ans


a = Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
