#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 5.最长回文子串.py
@time: 2020/4/3 11:19
@desc: 
"""
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
