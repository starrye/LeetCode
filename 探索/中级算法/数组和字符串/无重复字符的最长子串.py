# encoding: utf-8
"""
@Project ： 
@File: 无重复字符的最长子串.py
@Author: liuwz
@time: 2022/1/10 6:29 下午
@desc: 
"""


"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        dict_ = {}
        for i, v in enumerate(s):
            left = max(left, dict_.get(v, -2) + 1)
            dict_[v] = i
            max_len = max(max_len, i - left + 1)
        return max_len


a = Solution().lengthOfLongestSubstring('abcabcbb')
print(a)


