#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 77. 组合.py
@time: 2020/9/8 10:09
@desc: 
"""
from typing import List
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from itertools import combinations, permutations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # 回溯
        # result = []
        # # current_list:当前已经组装好的组合 start:这次要组装剩下的数中开始位置
        # def help(current_list, start):
        #     # 当已经组装好的组合长度==k 加入到最终结果，然后跳出本次递归，返回上次递归的调用位置
        #     if len(current_list) == k:
        #         result.append(current_list[:])
        #         return
        #     for i in range(start, n+1):
        #         # 选择当前数字
        #         current_list.append(i)
        #         # 进入递归
        #         help(current_list, i+1)
        #         # 撤销选择
        #         current_list.pop()
        # # 从1开始进入递归
        # help([], 1)
        # return result

        # python内置库
        # combinations方法重点在组合，permutations方法重在排列
        # combinations不在意顺序，而permutations有顺序
        return list(combinations([i+1 for i in range(n)], k))

a = Solution().combine(4, 2)
print(a)