# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 48. 最长不含重复字符的子字符串.py
@Author: liuwz
@time: 2022/1/6 7:41 下午
@desc: 
"""


"""
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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_ = dict()
        cur_len = 0
        max_len = 0
        for i, v in enumerate(s):
            index = dict_.get(v, -1)
            dict_[v] = i
            if cur_len < i - index:
                cur_len += 1
            else:
                cur_len = i - index
            max_len = max(cur_len, max_len)
        return max_len


a = Solution().lengthOfLongestSubstring("abba")
print(a)
