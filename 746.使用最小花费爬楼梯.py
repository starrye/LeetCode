#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 746.使用最小花费爬楼梯.py
@time: 2020/2/25 16:48
@desc: 
"""
"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
示例 1:
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
注意：
cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 问题拆解
        # 对于阶梯i，由于一次可以上一阶或两阶，因此必定需要从i - 1阶或i - 2阶上来(0, 1阶除外，这是边界) min(dp[i-1], dp[i-2])
        # 公式
        # dp[i] = cos[i]   i =0,1
        # dp[i] = min(dp[i-1],dp[i-2]) + cos[i] i>1
        # !!!可能会有人迷惑 可以选择从索引为 0 或 1 的元素作为初始阶梯 这一点，其实可以当做从平地作为起点，登一步到阶梯0，两步到阶梯1
        # dp 走到该索引+1层需要的最小体力
        # dp[0] 走到第一层的消耗体力
        # dp[1] 走到第二层的消耗体力 一定 =cost[1]
        dp = cost[:2]  # 固定选择第一层或者第二层
        for i in range(2, len(cost)):
            dp.append(min(dp[i-1], dp[i-2]) + cost[i])
        return min(dp[-1], dp[-2])

a = Solution().minCostClimbingStairs([1,2])
print(a)