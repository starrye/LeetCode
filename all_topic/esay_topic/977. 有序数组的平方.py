#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 977. 有序数组的平方.py
@time: 2020/10/16 10:11
@desc: 
"""
from typing import List
"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
 

提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
"""


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # A = sorted(A, key=lambda x:abs(x))
        # return [i**2 for i in A]

        # return sorted([i**2 for i in A])

        # 双指针
        n = len(A) - 1
        ans = [0] * (n + 1)
        i, j, index = 0, n, n
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                ans[index] = A[i] ** 2
                i += 1
            else:
                ans[index] = A[j] ** 2
                j -= 1
            index -= 1
        return ans


a = Solution().sortedSquares([-4,-1,0,3,10])
print(a)