#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1.py
@time: 2020/4/18 14:57
@desc: 
"""
class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        count = 0
        for i in coins:
            if i % 2:
                count += i//2 + 1
            else:
                count += i // 2
        return count


a = Solution().minCount([4,2,1])
print(a)