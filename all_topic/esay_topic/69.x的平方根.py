#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 69.x的平方根.py
@time: 2020/5/9 08:58
@desc: 
"""
from typing import List

"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        i = 0
        j = x // 2
        result = 0
        while i <= j:
            mid = (i + j) // 2
            if mid*mid < x:
                result = max(mid, result)
                i = mid + 1
            elif mid*mid == x:
                return mid
            elif mid*mid > x:
                j = mid - 1
        return result


        # return int(x**0.5)


a = Solution().mySqrt(4)
print(a)