#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 459.重复的子字符串.py
@time: 2020/4/3 16:37
@desc: 
"""
"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。
示例 2:
输入: "aba"
输出: False
示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # length = len(s)
        # for i in range(1, length//2 + 1):
        #     if not (length % i):
        #         if s[:i] * (length//i) == s:
        #             return True
        # return False

        # 如果字符串不是由重复的字串构成 那么ss从第二个字符开始查找s的话 必然只能找到第二个 而且返回的位置应该是第二个s的终点索引 也即是第一个s的长度
        # return (s+s).find(s, 1) != len(s)

        # 如果字符串不是由重复的字串构成 那么s必然不存在于 s[1:]s[:-1]
        return s in s[1:]+s[:-1]


a = Solution().repeatedSubstringPattern("abc")
print(a)