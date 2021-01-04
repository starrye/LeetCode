#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 152. 乘积最大子数组.py
@time: 2020/5/18 09:32
@desc: 
"""
import math
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 正向求积
        pre_product = 0
        inverted_product = 0
        max_product = float("-inf")
        for i in range(len(nums)):
            pre_product = (pre_product or 1) * nums[i]
            inverted_product = (inverted_product or 1) * nums[~i]
            max_product = max(pre_product, inverted_product, max_product)
        return max_product

a = Solution().maxProduct([2,3,-2,4])
print(a)


