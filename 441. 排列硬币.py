#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 441. 排列硬币.py
@time: 2020/2/21 15:44
@desc: 
"""
"""
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
给定一个数字 n，找出可形成完整阶梯行的总行数。
n 是一个非负整数，并且在32位有符号整型的范围内。
示例 1:
n = 5
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤
因为第三行不完整，所以返回2.
示例 2:
n = 8
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
因为第四行不完整，所以返回3.
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 首先 1行 1个 2行 2个
        # 利用等差求和公式 n(n+1)/2 可以求出n行的硬币总数是n(n+1)/2
        # 利用不等式 i(i+1)/2 >= n
        # 利用 int转化可以求出 临界整数
        return int((2*n+0.25)**0.5-0.5)

a = Solution().arrangeCoins(9)
print(a)