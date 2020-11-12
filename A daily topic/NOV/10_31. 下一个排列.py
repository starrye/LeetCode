#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 31. 下一个排列.py
@time: 2020/11/10 14:05
@desc: 
"""
import bisect
from typing import List
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        # 记录是否存在下一个更大的排列
        begin = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                # 第一种情况：最后两个数颠倒位置
                if i == len(nums) - 2:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    return nums
                # 第二种情况：排序后找到可以替换当前位置的数字
                else:
                    self.reverse(nums, begin)
                    # 这里不实用切片是因为不符合空间要求为1
                    # nums[begin:] = sorted(nums[begin:])
                    j = bisect.bisect(nums, nums[begin - 1], lo=begin)
                    # for j in range(begin, len(nums)):
                    #     if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    return nums
            else:
                begin = i
        if begin == 0:
            self.reverse(nums)
            return nums

    def reverse(self, nums, begin=0):
        length = len(nums) - 1
        while begin < length:
            nums[begin], nums[length] = nums[length], nums[begin]
            begin += 1
            length -= 1

a = Solution().nextPermutation([1,3,2])
print(a)


