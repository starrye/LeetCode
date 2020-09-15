#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 125. 验证回文串.py
@time: 2020/8/10 14:24
@desc: 
"""
import re
from typing import List
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # str_list = re.findall("[a-z0-9]+", s.lower().strip())
        # new_str = "".join(str_list)
        # length = len(new_str) - 1
        # print(new_str[:length//2])
        # print(new_str[-1:length//2+length % 2-1:-1])
        # return new_str[:length//2] == new_str[-1:length//2+length % 2-1:-1]

        if len(s) == 0:
            return False
        if len(s) == 1:
            return True
        n = len(s) - 1
        i = 0
        while i <= n:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[n].isalnum():
                n -= 1
                continue
            if s[i].lower() != s[n].lower():
                return False
            i += 1
            n -= 1
        return True

# a = Solution().isPalindrome("A man, a plan, a canal: Panama")
# b = Solution().isPalindrome("race a car")
c = Solution().isPalindrome("aa")
# print(a)
# print(b)
print(c)
