#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 204. 计数质数.py
@time: 2020/8/31 14:32
@desc: 
"""
from typing import List
"""
统计所有小于非负整数 n 的质数的数量。
示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""
from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        # 埃拉托色尼筛选法
        # 首先我们找到第一个素数2，用圆圈标出来，然后划掉所有2的倍数4、6、8等等。
        # 然后我们找到下一个没有被划掉的数字（这个数字肯定不是前面更小数字的倍数），也就是3，用圆圈标出来，
        # 再划掉所有的3的倍数，注意这里6已经被划掉了，但是9可以继续被划掉。
        # 接下来再用圆圈标出下一个没有被划掉的数字5，划掉所有的5的倍数。
        # 如此往复，直到100的平方根10截止，所有的100以内的素数就都被圆圈圈起来了

        if n < 2:
            return 0
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        sqrt_ = int(sqrt(n))
        for i in range(2, sqrt_ + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        result = 0
        for i in primes:
            if i:
                result += 1
        return result

a = Solution().countPrimes(10)
print(a)