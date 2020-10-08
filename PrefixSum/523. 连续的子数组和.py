#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 523. 连续的子数组和.py
@time: 2020/10/8 11:14
@desc: 
"""
from typing import List
"""
给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。
示例 1：
输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2：

输入：[23,2,6,4,7], k = 6
输出：True
解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
 

说明：

数组的长度不会超过 10,000 。
你可以认为所有数字总和在 32 位有符号整数范围内。
"""

from collections import defaultdict
import itertools

"""
可以被k整除的连续数组，只要保证sum[:j]和sum[:i]的对k的余数相等即可。
这里是 当有sum[:j] 与 sum[:i] 有相同余数时 则sum[:j] - sum[:i] 中元素(i到j-1)和正好是k的倍数，记录一下
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        current_sum = 0
        relation = {0: -1}
        for index, value in enumerate(nums):
            current_sum += value
            if k:
                current_sum %= k
            pre = relation.setdefault(current_sum, index)
            if index - pre > 1:
                return True
        return False
