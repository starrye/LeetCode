#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 680. 验证回文字符串 Ⅱ.py
@time: 2020/5/9 16:51
@desc: 
"""
from typing import List

"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 位运算！
        l = len(s)
        mid = l // 2
        if s[:mid] == s[-1:-1-mid:-1]:
            return True
        for i in range(mid):
            # ~ 按位取反 0 ~0=-1 1 ~1=-2 正好对应相应索引
            if s[i] != s[~i]:
                m = l + (~i)
                mid = (m-i) // 2
                return s[i:i+mid] == s[m-1:m-mid-1:-1] or s[i+1:i+mid+1] == s[m:m-mid:-1]
    #     # double pointers
    #     length = len(s)
    #     if length == 1:
    #         return True
    #     i = 0
    #     j = length - 1
    #     while i < j:
    #         if s[i] == s[j]:
    #             i += 1
    #             j -= 1
    #             continue
    #         return self.findPalindrome(s[i:j]) or self.findPalindrome(s[i+1:j+1])
    #     return True
    # def findPalindrome(self,s):
    #     length = len(s)
    #     i = 0
    #     j = length - 1
    #     while i < j:
    #         if s[i] != s[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #     return True


a = Solution().validPalindrome("aba")
print(a)