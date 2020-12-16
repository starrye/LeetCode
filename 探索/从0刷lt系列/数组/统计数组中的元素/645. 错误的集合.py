#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 645. 错误的集合.py
@time: 2020/5/9 09:11
@desc: 
"""
from typing import List

"""
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:

输入: nums = [1,2,2,4]
输出: [2,3]
注意:

给定数组的长度范围是 [2, 10000]。
给定的数组是无序的。
"""
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # repeat_num = None
        # nums.sort()
        # correct_sum = sum(range(1,len(nums)+1))
        # current_sums = sum(nums)
        # for i in range(len(nums)):
        #     if nums[i] == nums[i-1] and i != 0:
        #         repeat_num = nums[i]
        # return [repeat_num, correct_sum - current_sums + repeat_num]

        # 位运算！！！！
        idx = [i for i in range(1, len(nums)+1)]
        a, b = self.findTwoNums(nums+idx)
        if a in nums:
            return [a, b]
        return [b, a]

    def findTwoNums(self, nums):
        all_xor = 0
        for num in nums:
            all_xor ^= num
        mask = 1
        while all_xor & mask == 0:
            mask <<= 1
        a = 0
        for i in nums:
            if mask & i == 0:
                a ^= i
        return [a, all_xor ^ a]

a = Solution().findErrorNums([3,2,3,4,6,5])
b = Solution().findErrorNums([2,2])
c = Solution().findErrorNums([1,5,3,2,2,7,6,4,8,9])
print(a)
print(b)
print(c)
