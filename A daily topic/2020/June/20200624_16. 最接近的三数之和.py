#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 16. 最接近的三数之和.py
@time: 2020/6/24 09:51
@desc: 
"""
from typing import List
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = float("-inf")
        nums = sorted(nums)
        min_ = 1000
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            m = i+1
            n = len(nums)-1
            while m < n:
                tmp_sum = nums[i] + nums[m] + nums[n]
                # 差值
                d_value = tmp_sum - target
                if d_value == 0:
                    return target
                elif d_value > 0:
                    n -= 1
                elif d_value < 0:
                    m += 1
                a_d_value = abs(d_value)
                if a_d_value < min_:
                    min_ = a_d_value
                    result = tmp_sum
        return result

a = Solution().threeSumClosest([-1,2,1,-4], 1)
print(a)

