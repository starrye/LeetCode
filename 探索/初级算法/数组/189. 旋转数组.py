#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 189. 旋转数组.py
@time: 2020/8/3 11:28
@desc: 
"""
from typing import List
"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # length = len(nums)
        # nums[:] = nums[length-k:] + nums[:length-k]
        # print(nums)

        # for i in range(k):
        #     nums.insert(0, nums.pop())
        # print(nums)

        # length = len(nums)
        # k = k % length
        # nums.extend(nums[:length-k])
        # for i in range(length-k):
        #     nums.pop(0)
        # print(nums)
        length = len(nums)
        k %= length
        for i in range((length-k)//2):
            nums[i], nums[length-k-1-i] = nums[length-k-1-i], nums[i]
        for j in range(k // 2):
            nums[length - k + j], nums[length - j - 1] = nums[length - j - 1], nums[length - k + j]
        for k in range(length//2):
            nums[k], nums[length-k - 1] = nums[length-k - 1], nums[k]
        print(nums)
# a = Solution().rotate([1,2,3,4,5,6,7], 3)
b = Solution().rotate([1,2,3,4,5,6,7], 7)
