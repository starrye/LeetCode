#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1.py
@time: 2020/4/26 10:30
@desc: 
"""

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_sum = 0
        for index, val in enumerate(s):
            if index == 0:
                continue
            max_sum = max(max_sum, s[:index].count("0") + s[index:].count("1"))
        return max_sum

a = Solution().maxScore("11")
print(a)