# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 48. 最长不含重复字符的子字符串.py
@Author: liuwz
@time: 2022/4/6 12:02 下午
@desc: 
"""
""":cvar
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

s.length <= 40000
"""
import pandas as pd
import numpy as np


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        # left = right = 0
        # ans = 1
        # while left <= right < n - 1:
        #     right += 1
        #     try:
        #         left += s[left:right].index(s[right]) + 1
        #     except:
        #         pass
        #     finally:
        #         ans = max(ans, right - left + 1)
        # return ans

        dic = {}
        left = -1
        res = 0
        for right in range(n):
            if s[right] in dic:
                left = max(dic[s[right]], left)
            dic[s[right]] = right
            res = max(res, right - left)
        return res

a = Solution().lengthOfLongestSubstring("pwwkew")
print(a)

