#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 525. 连续数组.py
@time: 2020/10/8 13:50
@desc: 
"""
from typing import List
"""
给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。
示例 1:
输入: [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

注意: 给定的二进制数组的长度不会超过50000。
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # ans = 0
        # current_sum = 0
        # result = {}
        # for index, value in enumerate(nums):
        #     if value == 0:
        #         current_sum += -1
        #     else:
        #         current_sum += 1
        #     if current_sum == 0:
        #         ans = index + 1
        #     else:
        #         if current_sum not in result:
        #             result[current_sum] = index
        #         else:
        #             ans = max(ans, index - result[current_sum])
        # return ans

        ans, current_sum, result = 0, 0, {0: -1}
        for index, value in enumerate(nums):
            current_sum += value if value else -1
            ans = max(ans, index - result.setdefault(current_sum, index))
        return ans
