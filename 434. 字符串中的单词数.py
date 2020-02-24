#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 434. 字符串中的单词数.py
@time: 2020/2/21 15:12
@desc: 
"""

"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
"""

class Solution:
    def countSegments(self,s:str) -> int:
        return len(s.split())

a = Solution().countSegments(", , , ,        a, eaefa")
print(a)