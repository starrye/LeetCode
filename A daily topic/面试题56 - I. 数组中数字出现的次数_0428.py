#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题56 - I. 数组中数字出现的次数.py
@time: 2020/4/28 09:03
@desc: 
"""
"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums <= 10000
"""
from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        all_xor = 0
        for num in nums:
            all_xor ^= num
        print(all_xor)
        mask = 1
        while all_xor & mask == 0:
            mask <<=1
        print(mask)
        a = 0
        for i in nums:
            if mask & i == 0:
                a ^= i
        return [a, all_xor ^ a]


a = Solution().singleNumbers([4,1,4,6])
b = Solution().singleNumbers([1,2,5,2])
print(a)
print(b)
