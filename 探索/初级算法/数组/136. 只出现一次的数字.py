#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 136. 只出现一次的数字.py
@time: 2020/5/14 09:27
@desc: 
"""
from typing import List
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from _functools import reduce
        return reduce(lambda x,y:x^y,nums)

        # single_num = nums[0]
        # for i in nums[1:]:
        #     single_num ^= i
        # return single_num


a = Solution().singleNumber([4,1,2,1,2])
print(a)