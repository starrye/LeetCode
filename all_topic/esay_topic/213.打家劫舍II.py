#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 213.打家劫舍II.py
@time: 2020/3/2 12:02
@desc: 
"""
"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 使用自定义函数分别对nums[1:] 与 nums[:-1] 求最大值
        # 然后最后去两种情况下的最大值（1.偷第一家  2.不偷第一家）
        def my_rob(nums):
            last_max = 0
            curr_max = 0
            for i in nums:
                curr_max, last_max = max(last_max + i, curr_max), curr_max
            return curr_max
        return max(my_rob(nums[1:]), my_rob(nums[:-1])) if len(nums) != 1 else nums[0]

a = Solution().rob([1,2,3,1])
print(a)