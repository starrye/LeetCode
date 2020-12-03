#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 204. 计数质数.py
@time: 2020/12/3 09:38
@desc: 
"""
from math import sqrt
from typing import List
"""
统计所有小于非负整数 n 的质数的数量。

 

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0
 

提示：

0 <= n <= 5 * 106
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True] * n
        sqrt_ = int(sqrt(n))
        for i in range(2, sqrt_ + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        result = 0
        for i in range(2, n):
            if primes[i]:
                result += 1
        return result