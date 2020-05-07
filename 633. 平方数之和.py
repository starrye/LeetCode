#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 633. 平方数之和.py
@time: 2020/5/6 15:55
@desc: 
"""
from typing import List

"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
示例1:
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
 
示例2:

输入: 3
输出: False

"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c ** 0.5)
        while i <= j:
            current_sum = i*i + j*j
            if current_sum == c:
                return True
            elif current_sum > c:
                j -= 1
            elif current_sum < c:
                i += 1
        return False

a = Solution().judgeSquareSum(10)
print(a)
