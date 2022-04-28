# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 46. 把数字翻译成字符串.py
@Author: liuwz
@time: 2022/4/6 10:59 上午
@desc: 
"""
""":cvar
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231
"""
import pandas as pd
import numpy as np

class Solution:
    def translateNum(self, num: int) -> int:
        # s_num = str(num)
        # n = len(s_num)
        # if n <= 1:
        #     return 1
        # dp = [0] * (n+1)
        # dp[0], dp[1] = 1, 1
        # for i in range(2, n+1):
        #     if 10 <= int(s_num[i-2:i]) <= 25:
        #         dp[i] = dp[i-2] + dp[i-1]
        #     else:
        #         dp[i] = dp[i-1]
        #     print(dp)
        # return dp[-1]

        n = len(str(num))
        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a + b if 10 <= int(str(num)[i-2:i]) <= 25 else b
        return b



a = Solution().translateNum(25)
print(a)