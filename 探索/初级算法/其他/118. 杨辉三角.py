#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 118. 杨辉三角.py
@time: 2020/9/4 14:53
@desc: 
"""
from typing import List
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # ans = []
        # for i in range(numRows):
        #     temp = []
        #     if i == 0:
        #         temp.append(1)
        #         ans.append(temp)
        #         continue
        #     for j in range(i+1):
        #         if j == 0 or j == i:
        #             temp.append(1)
        #         else:
        #             temp.append(ans[i-1][j-1] + ans[i-1][j])
        #     ans.append(temp)
        # return ans

        # 每一行都是由上一行 结尾+0 与 前缀+0(本身)的和
        # 比如 1331 由 1210 + 0121得来
        # 比如 144641 由 13310 + 01331得来
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            ans.append([a+b for a, b in zip([0]+ans[-1], ans[-1]+[0])])
        return ans



a = Solution().generate(6)
print(a)

