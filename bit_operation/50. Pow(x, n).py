#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 50. Pow(x, n).py
@time: 2020/5/11 08:56
@desc: 
"""
from typing import List
"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 递归 + 快速幂
        # def quickPow(N):
        #     if N == 0:
        #         return 1
        #     y = quickPow(N//2)
        #     return y * y if not N % 2 else y * y * x
        # return quickPow(n) if n >= 0 else 1.0 / quickPow(-n)
        #
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return x
        # res = 1
        # tmp_n = abs(n)
        # while tmp_n:
        #     if tmp_n & 1:
        #        res *= x
        #     x *= x
        #     tmp_n >>= 1
        # return res if n > 0 else 1/res


        ans = 1
        a_n = abs(n)
        while a_n:
            if a_n & 1:
                ans *= x
            x *= x
            a_n >>= 1
        return ans if n > 0 else 1 / ans




a = Solution().myPow(2,10)
print(a)