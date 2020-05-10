#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 674. 最长连续递增序列.py
@time: 2020/5/9 15:10
@desc: 
"""
from typing import List

"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。
"""


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # dp
        if not nums:
            return 0
        length = len(nums)
        dp = [0] * length
        dp[0] = 1
        for i in range(1,length):
            if nums[i-1] < nums[i]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        return max(dp)


        # 更新开始点
        # begin = 0
        # max_long = 0
        # length = len(nums)
        # for i in range(length):
        #     if i == length - 1:
        #         max_long = max(max_long, i - begin + 1)
        #         break
        #     if nums[i] >= nums[i + 1]:
        #         max_long = max(max_long, i - begin + 1)
        #         begin = i + 1
        # return max_long


        # result = 1
        # max_long = 1
        # for i in range(len(nums)-1):
        #     if nums[i] < nums[i+1]:
        #         result += 1
        #     else:
        #         max_long = max(max_long, result)
        #         result = 1
        # return max(max_long, result)

a = Solution().findLengthOfLCIS([1,3,5,4,7])
b = Solution().findLengthOfLCIS([1,2,1,2,3,4])
c = Solution().findLengthOfLCIS([1,1,1])
print(a)
print(b)
print(c)