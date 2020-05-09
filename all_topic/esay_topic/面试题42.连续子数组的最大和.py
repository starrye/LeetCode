#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题42.连续子数组的最大和.py
@time: 2020/3/2 11:14
@desc: 
"""
"""
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。
示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
提示：
1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ans = nums[0]
        # sum = 0
        # for i in nums:
        #     sum = max(sum+i,i)
        #     ans = max(ans,sum)
        # return ans

        if len(nums) == 1:
            return nums[0]
        sum = 0
        max_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        return max_sum

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     if dp[i - 1] <= 0:
        #         dp[i] = nums[i]
        #     else:
        #         dp[i] = dp[i - 1] + nums[i]
        # return max(dp)
a = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(a)