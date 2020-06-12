#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 15. 三数之和.py
@time: 2020/6/12 10:12
@desc: 
"""
from typing import List
"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        if not nums or length < 3:
            return result
        nums.sort()
        for i in range(length):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                tmp = [nums[i], nums[left], nums[right]]
                if sum(tmp) == 0:
                    result.append(tmp)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum(tmp) > 0:
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                else:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
        return result

a = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(a)