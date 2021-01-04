#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 290. 单词规律.py
@time: 2020/12/16 10:14
@desc: 
"""
from typing import List
"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # pattern_list = [i for i in pattern]
        # s_list = s.split(" ")
        # if len(pattern_list) != len(s_list):
        #     return False
        # dict_ = {}
        # set_ = set()
        # for i in range(len(pattern_list)):
        #     if pattern_list[i] not in dict_:
        #         if s_list[i] not in set_:
        #             dict_[pattern_list[i]] = s_list[i]
        #             set_.add(s_list[i])
        #         else:
        #             return False
        #     elif dict_.get(pattern_list[i], None) != s_list[i]:
        #         return False
        # return True

        n = s.split()
        return len(set(zip(pattern, n))) == len(set(pattern)) == len(set(n)) if len(n) == len(pattern) else False


a = Solution().wordPattern("abba", "dog cat cat dog")
b = Solution().wordPattern("abba", "dog cat cat fish")
c = Solution().wordPattern("aaaa", "dog cat cat dog")
d = Solution().wordPattern("abba", "dog dog dog dog")
print(a)
print(b)
print(c)
print(d)