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
        # 1.数组中有一个负数 索引位置为i 那么最大值一定出自nums[:i]与nums[i+1:]中
        # 2.两个负数 最大值一定是全部乘积(有0就0左与0右)
        # 3.三个负数 最大值是max(nums[:第三个负数索引],nums[-1:第一个负数索引]抽象理解 真实索引不是这样)）
        # 那就是只讨论负数个数为奇数的情况下最大值来自哪里 max(正向:nums[0:最后一个负数索引],负向:nums[-1:-第一个负数的索引]）
        # 那只要遍历的nums的过程中 把正向到i与负向到(-i-1)[这里就是~i]的位置积求出来 是不是最大值一定藏在里面

        # pre_product = 0
        # inverted_product = 0
        # max_product = float("-inf")
        # for i in range(len(nums)):
        #     pre_product = (pre_product or 1) * nums[i]
        #     inverted_product = (inverted_product or 1) * nums[~i]
        #     max_product = max(pre_product, inverted_product, max_product)
        # return max_product

        # dp
        current_max_product = 0
        current_min_product = 0
        max_product = float("-inf")
        for i in range(len(nums)):
            if nums[i] < 0:
                current_max_product, current_min_product = current_min_product, current_max_product
            current_max_product = max(current_max_product*nums[i], nums[i])
            current_min_product = min(current_min_product*nums[i], nums[i])
            max_product = max(current_max_product, max_product)
        return max_product

a = Solution().maxProduct([2,3,-2,4])
print(a)


