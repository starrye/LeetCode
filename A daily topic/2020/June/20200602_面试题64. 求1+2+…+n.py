#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题64. 求1+2+…+n.py
@time: 2020/6/2 09:54
@desc: 
"""
from typing import List
"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
示例 1：
输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000
"""

class Solution:
    def sumNums(self, n: int) -> int:
        return n and n+self.sumNums(n-1)

a = Solution().sumNums(6)
print(a)
