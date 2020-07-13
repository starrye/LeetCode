#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 309. 最佳买卖股票时机含冷冻期.py
@time: 2020/7/10 08:48
@desc: 
"""
from typing import List
"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""

# dp[i] = max(dp[i-1]+prices[i]-proces[i-1], )
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass

