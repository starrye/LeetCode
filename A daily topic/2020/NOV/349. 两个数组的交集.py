#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 349. 两个数组的交集.py
@time: 2020/11/2 15:19
@desc: 
"""
from typing import List
"""
给定两个数组，编写一个函数来计算它们的交集。
示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
 

说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1)&(set(nums2)))

        return list(set(nums1).intersection(nums2))


a = Solution().intersection([4,9,5], [9,4,9,8,4])
print(a)