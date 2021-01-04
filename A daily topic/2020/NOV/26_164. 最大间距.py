#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 164. 最大间距.py
@time: 2020/11/26 09:51
@desc: 
"""
from typing import List
"""

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
"""
# 基于桶排序
# 每个桶的长度确立： max(nums) - min(nums) / len(nums) - 1
# 桶的数量

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        n = len(nums)
        max_num, min_num = max(nums), min(nums)
        each_bucket_length = max(1, (max_num - min_num) // (n - 1))
        buckets = [[] for _ in range((max_num - min_num) // each_bucket_length + 1)]
        result = 0

        for i, v in enumerate(nums):
            index = (v - min_num) // each_bucket_length
            buckets[index].append(v)

        pre_max = float("inf")
        for i in range(len(buckets)):
            if buckets[i] and pre_max != float("inf"):
                result = max(result, min(buckets[i]) - pre_max)

            if buckets[i]:
                pre_max = max(buckets[i])

        return result

a = Solution().maximumGap([3,6,9,1])
print(a)