#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1480. 一维数组的动态和.py
@time: 2020/6/15 10:38
@desc: 
"""
from typing import List
"""
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
请返回 nums 的动态和。
示例 1：

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
示例 2：

输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
示例 3：

输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]
 

提示：

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if not result:
                result.append(num)
            else:
                result.append(num + result[-1])
        return result
