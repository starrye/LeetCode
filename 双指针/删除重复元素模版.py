#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 删除重复元素模版.py
@time: 2020/10/8 15:33
@desc: 
"""
from typing import List

# 删除排序数组重复元素，且重复元素最多重复k个

def removeDuplicates(nums, k: int) -> int:
    l = len(nums)
    if l <= k:
        return l
    i = k # 指向当前要拷贝覆盖的索引位置
    for j in range(k, len(nums)):
        if nums[j] != nums[i - k]:
            nums[i] = nums[j]
            i += 1 # 指向下一个要覆盖的索引位置
    return i
# 2: 双指针(基于计数) -- 删除排序数组重复元素，且重复元素最多重复k个

def removeDuplicates(nums, k: int) -> int:
    l = len(nums)
    if l <= k: # 特判
        return l
    i, count = 0, 1
    for j in range(1, len(nums)):
        if nums[j] == nums[i]: # 重复则计算加1
            count += 1
        else: # 否则，计数重置
            count = 1

        if count <= k:
            i += 1
            nums[i] = nums[j]
    return i + 1
