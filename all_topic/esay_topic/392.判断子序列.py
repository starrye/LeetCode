#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 392.判断子序列.py
@time: 2020/2/28 14:15
@desc: 
"""
"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
示例 1:
s = "abc", t = "ahbgdc"
返回 true.
示例 2:
s = "axc", t = "ahbgdc"
返回 false.
后续挑战 :
如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 短串(s)为空 一定是t的子序列
        if s == "":
            return True
        elif t == "":
            # 进入此判断说明 短串(s)不为空 长串（t）为空 一定不是t的子序列
            return False
        for i in s:
            if i in t:
                # 从此位置的下一位开始判断
                t = t[t.index(i)+1:]
            else:
                return False
        return True

        # 双指针
        # n, m = len(s), len(t)
        # i = j = 0
        # while i < n and j < m:
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == n


        # 题解 find函数
        # if s == '':
        #     return True
        # loc = -1
        # for i in s:
        #      这里的find 表示从 t的loc + 1位开始寻找i 等同于 从t[loc+1:] 开始寻找i
        #     loc = t.find(i, loc + 1)
        #     if loc == -1:
        #         return False
        # return True



a = Solution().isSubsequence("","ahbgdc")
print(a)