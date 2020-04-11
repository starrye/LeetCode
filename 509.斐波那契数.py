#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 509.斐波那契数.py
@time: 2020/4/7 16:55
@desc: 
"""
"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。
示例 1：
输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：
输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：
输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
 
提示：
0 ≤ N ≤ 30
"""

"""
思路分析（个人理解，只是记录下来 hha）：
1.斐波那契常规处理中(倒序计算)会重复计算，这也是时间消耗较长的原因
2.利用动态规划正序推导，计算每一项的值（虽然利用前两项的值，但由于列表已经保存，直接索引就可以获得）
3.循环(终止条件:<=N 从2开始>)，然后输出最后一个值就是当前项的值
"""


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 动态规划1
        # if N == 0:
        #     return 0
        # elif N == 1:
        #     return 1
        # opt = [0] * (N+1)
        # opt[0] = 0
        # opt[1] = 1
        # i = 2
        # while i <= N:
        #     opt[i] = opt[i-1] + opt[i-2]
        #     print(opt)
        #     i += 1
        # return opt[-1]

        # 动态规划2
        dp_1, dp_2 = 0, 1
        for _ in range(2, N+1):
            dp_1, dp_2 = dp_2, dp_1+dp_2
        return dp_2

a = Solution().fib(4)
print(a)