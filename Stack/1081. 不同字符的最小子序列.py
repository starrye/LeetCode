# encoding: utf-8
"""
@author: liuwz
@time: 2021/3/29 2:03 下午
@file: 1081. 不同字符的最小子序列.py
@desc: 
"""
import collections

"""
返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。

注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同
示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：
1 <= s.length <= 1000
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