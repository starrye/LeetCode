#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 922. 按奇偶排序数组 II.py
@time: 2020/11/12 09:49
@desc: 
"""
from typing import List
"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # odd_list = []
        # even_list = []
        # for i in range(len(A)):
        #     # 奇数放到了偶数位置
        #     if A[i] & 1 and not (i & 1):
        #         odd_list.append(i)
        #     # 偶数放到了奇数位置
        #     elif not (A[i] & 1) and i & 1:
        #         even_list.append(i)
        # for j in range(len(odd_list)):
        #     A[odd_list[j]], A[even_list[j]] = A[even_list[j]], A[odd_list[j]]
        # return A

        i, j, length = 0, 1, len(A)-1
        while i <= length and j <= length:
            while i <= length and not(A[i] & 1):
                i += 2
            while j <= length and (A[j] & 1):
                j += 2
            if i <= length and j <= length:
                A[i], A[j] = A[j], A[i]
        return A



a = Solution().sortArrayByParityII([4,2,5,7])
print(a)

