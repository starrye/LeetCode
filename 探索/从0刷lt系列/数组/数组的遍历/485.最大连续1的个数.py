#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 485.最大连续1的个数.py
@time: 2020/4/7 10:43
@desc: 
"""
"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：
输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #
        max_continuous_length = 0
        continuous_length = 0
        for i in range(len(nums)):
            if nums[i]:
                continuous_length += 1
            else:
                if continuous_length > max_continuous_length:
                    max_continuous_length = continuous_length
                continuous_length = 0
        return max(max_continuous_length, continuous_length)

        
        # 遍历得到每个位置的当前连续1的个数
        # current_continuous_length = [0]*len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         current_continuous_length[i] = current_continuous_length[i-1] + 1
        #     else:
        #         current_continuous_length[i] = 0
        # return max(current_continuous_length)


a = Solution().findMaxConsecutiveOnes([1,1,0,1,1,1,1])
print(a)