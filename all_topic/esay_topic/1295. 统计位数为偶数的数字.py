#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1295. 统计位数为偶数的数字.py
@time: 2020/5/12 17:00
@desc: 
"""
from typing import List
"""
给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。

示例 1：

输入：nums = [12,345,2,6,7896]
输出：2
解释：
12 是 2 位数字（位数为偶数） 
345 是 3 位数字（位数为奇数）  
2 是 1 位数字（位数为奇数） 
6 是 1 位数字 位数为奇数） 
7896 是 4 位数字（位数为偶数）  
因此只有 12 和 7896 是位数为偶数的数字
示例 2：

输入：nums = [555,901,482,1771]
输出：1 
解释： 
只有 1771 是位数为偶数的数字。
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # even_count = 0
        # for i in nums:
        #     if not len(str(i)) & 1:
        #         even_count += 1
        # return even_count
        return sum(1 for num in nums if not len(str(num))%2)

a = Solution().findNumbers([12,345,2,6,7896])
print(a)
