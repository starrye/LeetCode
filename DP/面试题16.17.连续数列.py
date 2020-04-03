#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题16.17.连续数列.py
@time: 2020/2/28 17:15
@desc: 
"""
"""
给定一个整数数组（有正数有负数），找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        解题思路：
            1.首先建立一个列表dp=[0]*len(nums)
            2.指定第一个元素dp[1] = nums[0]
            3.循环nums，如果dp上一个值小于等于0则更新dp[i] = nums[i]
            否则dp[i] = dp[i-1] + nums[i]
            4.返回dp最大值（dp内存储着到当前位置的最大总和）
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)

a = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(a)