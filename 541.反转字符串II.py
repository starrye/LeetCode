#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 541.反转字符串II.py
@time: 2020/4/17 17:17
@desc: 
"""
"""
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:
该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            return s[::-1]
        elif k <= len(s) < 2*k:
            return s[k-1::-1]+s[k:]
        else:
            s_new = ""
            i = 0
            # while i <=
            print(s[i*k*2+k-1:i*k*2-1:-1])
            for i in range(0, len(s)//(2*k)):
                # 2 -- 3
                # 0 1
                print(s[i*k*2+k-1:i*k*2-1:-1]+s[i*k*2+k:i*k*2+k*2])
                # s_new += s[k*i - 1::-1] + s[k*i:2 * k]
            # s_new += s[len(s)-len(s) % (2*k):]
        # return s_new


a = Solution().reverseStr("abdcdefghij", 2)
print(a)