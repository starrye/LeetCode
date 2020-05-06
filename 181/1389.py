#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1389.py
@time: 2020/4/30 10:07
@desc: 
"""


class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


# a = Solution().createTargetArray([0,1,2,3,4],[0,1,2,2,1])
# b = Solution().createTargetArray([1,2,3,4,0],[0,1,2,3,0])
c = Solution().createTargetArray([1],[0])
# print(a)
# print(b)
print(c)