#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 167. 两数之和 II - 输入有序数组.py
@time: 2020/7/20 09:40
@desc: 
"""
from typing import List
"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dict_ = {}
        # for k,v in enumerate(numbers):
        #     if v in dict_:
        #         return [dict_[target-v], k+1]
        #     dict_[target-v] = k + 1

        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                break
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return [i + 1, j + 1]



