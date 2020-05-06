#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1390.py
@time: 2020/4/30 10:13
@desc: 
"""


class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result += self.find_yinzi(i)
        return result

    def find_yinzi(self, num):
        result = set()
        for i in range(1, int(num**0.5) + 1):
            if len(result) > 4:
                return 0
            if num % i == 0:
                result.add([i,num // i])
        if len(result) == 4:
            return sum(result)
        return 0
