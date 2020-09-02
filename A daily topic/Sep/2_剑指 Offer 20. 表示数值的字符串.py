#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 剑指 Offer 20. 表示数值的字符串.py
@time: 2020/9/2 09:37
@desc: 
"""
from typing import List
"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

"""

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False