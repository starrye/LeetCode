#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 453. 最小移动次数使数组元素相等.py
@time: 2020/2/24 17:06
@desc: 
"""
"""
给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。
示例:
输入:
[1,2,3]
输出:
3
解释:
只需要3次移动（注意每次移动会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n-1个元素增加1 --> 1个元素减1 相对论
        rn = 0
        min_n = min(nums)
        for i in nums:
            rn += i - min_n
        return rn
