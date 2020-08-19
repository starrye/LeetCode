#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 647. 回文子串.py
@time: 2020/8/19 10:15
@desc: 
"""
from typing import List
"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串
示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

提示：

输入的字符串长度不会超过 1000 。
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        ans = 0
        for i in range(len(s)):
            for j in range(i+1):
                if i == j:
                    dp[i][j] = True
                    ans += 1
                elif i - j == 1 and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1
                elif i - j > 1 and s[i] == s[j] and dp[i-1][j+1]:
                    dp[i][j] = True
                    ans += 1
        return ans


a = Solution().countSubstrings("aba")
print(a)