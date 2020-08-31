#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 70.爬楼梯.py
@time: 2020/2/25 16:46
@desc: 
"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # a = 1
        # b = 2
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # for i in range(3,n+1):
        #     a,b = b,a+b
        # return b

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

a = Solution()
print(a.climbStairs(12))