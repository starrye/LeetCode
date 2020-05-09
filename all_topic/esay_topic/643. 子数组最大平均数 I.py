#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 643. 子数组最大平均数 I.py
@time: 2020/5/8 17:41
@desc: 
"""
from typing import List

"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
示例 1:
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


注意:

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        tmp_sum = sum(nums[:k])
        for i in range(len(nums)-k):
            max_sum = max(max_sum, tmp_sum-nums[i]+nums[i+k])
            tmp_sum += nums[i + k] - nums[i]
        return max_sum / k

a = Solution().findMaxAverage([1,12,-5,-6,50,3],4)
print(a)
