#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 738. 单调递增的数字.py
@time: 2020/12/15 10:13
@desc: 
"""
from typing import List

"""
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N 是在 [0, 10^9] 范围内的一个整数。
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        从前往后遍历，找到第一个当前值小于上一个值的位置，然后倒序更改 ： 当前位置变9 前一个位置-1 知道符合规则 然后当前位置后面的数字都变9 注意第一个数为0的情况
        :param N:
        :return:
        """
        if N < 10:
            return N
        list_n = list(str(N))
        length = len(list_n)
        flag = None
        pre_n = list_n[0]
        for i in range(length):
            if int(list_n[i]) < int(pre_n):
                flag = i
                break
            pre_n = list_n[i]
        if not flag:
            return N
        else:
            while i >= 1 and int(list_n[i]) < int(list_n[i - 1]):
                list_n[i] = "9"
                list_n[i - 1] = str(int(list_n[i - 1]) - 1)
                i -= 1
            list_n = list_n[:i + 1] + ["9"] * (length - i - 1)
            return int(''.join(list_n)) if list_n[0] != 0 else int(''.join(list_n[1:]))


a = Solution().monotoneIncreasingDigits(4562)
print(a)


