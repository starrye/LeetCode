# encoding: utf-8
"""
@author: liuwz
@time: 2021/3/29 2:01 下午
@file: 316. 去除重复字母.py
@desc: 
"""
import collections

"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 104
s 由小写英文字母组成

"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        dict_ = collections.Counter(s)
        for i in s:
            if i not in stack:
                while stack and i < stack[-1] and dict_[stack[-1]] > 0:
                    stack.pop()
                stack.append(i)
            dict_[i] -= 1
        return "".join(stack)