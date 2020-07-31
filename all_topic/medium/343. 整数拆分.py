#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 343. 整数拆分.py
@time: 2020/7/30 09:51
@desc: 
"""
from typing import List
"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        # if n == 2:
        #     return 1
        # elif n == 3:
        #     return 2
        # elif n == 4:
        #     return 4
        # elif n == 5:
        #     return 6
        # ans = 1
        # while n > 4:
        #     ans *= 3
        #     n -= 3
        # ans *= n
        # return ans
        dp = [1, 1, 1, 2, 4, 6, 9]
        if n <= 6:
            return dp[n]
        for i in range(7, n + 1):
            dp.append(dp[i - 3] * 3)
        return dp[-1]


a = Solution().integerBreak(10)
print(a)


