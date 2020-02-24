#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 448. 找到所有数组中消失的数字.py
@time: 2020/2/24 16:25
@desc: 
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1))-set(nums))


a = Solution().findDisappearedNumbers([1,2,1])
print(a)