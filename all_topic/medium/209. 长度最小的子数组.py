#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 209. 长度最小的子数组.py
@time: 2020/6/28 09:18
@desc: 
"""
from typing import List
"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len = float("-inf")
        current_sum = 0
        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= s:
                min_len = min(min_len, right-left+1)
                current_sum -= nums[left]
                left += 1
        return min_len if min_len != float("-inf") else 0
