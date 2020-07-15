#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 96. 不同的二叉搜索树.py
@time: 2020/7/15 09:44
@desc: 
"""
from typing import List
"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""

class Solution:
    def numTrees(self, n: int) -> int:
        # 动态规划
        # 假设n个节点存在二叉排序树的个数是G(n),以i为根节点的二叉排序树个数为f(i)
        # 则G(n) = f(1) + f(2) + ... + f(n)
        # 以i为根节点的二叉排序树个数为 左子树可形成二叉排序的个数+右子树的二叉排序树的个数 左子树个数为i-1节点 右子树个数为n-i个节点
        # f(i) = G(i-1)*G(n-i)
        # 则 G（n） = G(0)*G(n-1) + G(1)*G(n-2) + .... + G(n)*G(0)
        # 定义初始值
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            # dp(i) = dp[0]*dp[i-1] + dp[1]*dp[i-2] + ... + dp[i-1]*dp[0]
            # dp(i)依赖于dp(0)..dp(i-1)
            # 观察有重复 可去重减少遍历次数
            for j in range(1, (i+2)//2):
                dp[i] += dp[j-1] * dp[i-j]
            # i为偶数结果*2
            dp[i] *= 2
            # i为奇数 要加上 dp[i//2] ** 2 这次 二次方是因为中间位置为dp[i//2]*dp[i//2]
            if i%2:
                dp[i] += dp[i//2] ** 2
        return dp[-1]