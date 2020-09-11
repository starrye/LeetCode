#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 216. 组合总和 III.py
@time: 2020/9/11 10:18
@desc: 
"""
from typing import List
"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
说明：
所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 回溯
        # result = []
        # def help(current_list, start):
        #     for i in range(start, 10):
        #         current_len = len(current_list)
        #         current_sum = sum(current_list)
        #         if current_len == k or i > n:
        #             return
        #         if current_sum + i == n and current_len + 1 == k:
        #             result.append(current_list + [i])
        #             return
        #         else:
        #             help(current_list + [i], i + 1)
        # help([], 1)
        # return result

        # 优化回溯
        result = []

        def help(current_list, start, k, n):
            for i in range(start, 10):
                if not k or i > n:
                    return
                if i == n and not (k - 1):
                    result.append(current_list + [i])
                    return
                else:
                    help(current_list + [i], i + 1, k - 1, n - i)
        help([], 1, k, n)
        return result

a = Solution().combinationSum3(2, 3)
print(a)