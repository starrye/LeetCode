#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1025.除数博弈.py
@time: 2020/2/28 14:37
@desc: 
"""
"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。
只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
示例 1：
输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。

提示：
1 <= N <= 1000
"""
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # dp思维
        """
        n = 1时输  
        n = 2时赢
        n=3之后 爱丽丝如果想赢就要找到一个小于n的数x 满足 N % x ==0的基础上 还要让下一个人直接输掉 也就是 N-x 先走的输
         满足 dp[i-j] == False and i(n) % j(x) ==0
        """
        # dp = {}
        # dp[1] = False
        # dp[2] = True
        # # 这里的i就是N j就是选择的x
        # for i in range(3,N+1):
        #     dp[i] = False
        #     for j in range(1,i):
        #         if dp[i-j] == False and i % j == 0:
        #             dp[i] = True
        #             break
        # return dp[N]

        # 数学归纳法
        """
        n = 1时输  
        n = 2时赢
        n = 3时输
        n = 4时赢
        。。。。归纳 n=偶数 赢 n=奇数输
        """
        # return N&1==0
        return N%2==0
a = Solution().divisorGame(4)
print(a)

