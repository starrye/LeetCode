#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 46.全排列.py
@time: 2020/4/25 14:23
@desc: 
"""
"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def travelback(tmp_list):
            if len(tmp_list) == nums_length:
                result.append(tmp_list[:])
                return
            for i in nums:
                if i in tmp_list:
                    continue
                tmp_list.append(i)
                travelback(tmp_list)
                tmp_list.pop()
        result = []
        nums_length = len(nums)
        travelback([])
        return result


a = Solution().permute([1,2,3])
print(a)