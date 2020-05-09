#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题 08.11.硬币.py
@time: 2020/4/23 09:23
@desc: 
"""
"""
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
示例1:
输入: n = 5
输出：2
解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

输入: n = 10
输出：4
解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：
注意:
你可以假设：
0 <= n (总金额) <= 1000000
"""


class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 这个问题是两个非常经典的问题的组合，其一是「完全背包问题」，其二是「背包方案数问题」
        # dp[i][j] 使用前i种硬币计算j分的表示法种数 令coins=[25, 10, 5, 1]
        # 状态转移方程的推导：
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-coins[i]] + dp[i-1][j-2coins[i]] + ... dp[i-1][j-kcoins[i]]
        # dp[i][j-coins[i]] = dp[i-1][j-coins[i]] + dp[i-1][j-2coins[i]] + ... dp[i-1][j-kcoins[i]]
        # dp[i][j] - dp[i][j-coins[i]] = dp[i-1][j]
        # dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j]
        coins = [1,5,10,25]
        dp = [[0 for _ in range(n+1)] for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1

        for i in range(1, len(coins)+1):
            for j in range(1, n+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j - coins[i-1]] + dp[i - 1][j]
        return dp[-1][-1] % 1000000007


a = Solution().waysToChange(5)
print(a)