#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题08.01.三步问题.py
@time: 2020/2/28 16:43
@desc: 
"""
"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。
实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:
 输入：n = 3 
 输出：4
 说明: 有四种走法
示例2:
 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间
"""
class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp思想
        """
        走上n层台阶可以从 n-3 走上来 也可以 n-2 走上来  n-1 走上来 所以走上n层台阶等于 3中情况的总和
        """
        # dp = {}
        # dp[1] = 1
        # dp[2] = 2
        # dp[3] = 4
        # if n > 3:
        #     for i in range(4,n+1):
        #         dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%1000000007
        # return dp[n]
        prepre, pre, now = 0, 0, 1
        for i in range(n):
            now, pre, prepre = (prepre+pre+now) % 1000000007, now, pre
        return now

a = Solution().waysToStep(10000)
print(a)
