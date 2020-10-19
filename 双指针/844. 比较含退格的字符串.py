#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 844. 比较含退格的字符串.py
@time: 2020/5/14 10:21
@desc: 
"""
from typing import List
"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

 

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
示例 4：

输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。
 

提示：

1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。
 

进阶：

你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
    #     tmp_s = self.tmp_str(S)
    #     tmp_t = self.tmp_str(T)
    #     return tmp_s == tmp_t
    #
    # def tmp_str(self, tmp_str):
    #     tmp_s = ""
    #     for i in range(len(tmp_str)):
    #         if tmp_str[i] != "#":
    #             tmp_s += tmp_str[i]
    #         else:
    #             tmp_s = tmp_s[:-1]
    #     return tmp_s

        # 双指针
        # 思路: 1. 倒序 一个一个对比 2.记录# 的数量 如果 > 0则跳过当前值 直接索引-1，直到找到不应该被删除的字符
        s_index = len(S) - 1
        t_index = len(T) - 1
        s_skip, t_skip = 0, 0
        while s_index >= 0 or t_index >= 0:
            while s_index >= 0:
                if S[s_index] == "#":
                    s_index -= 1
                    s_skip += 1
                elif s_skip > 0:
                    s_skip -= 1
                    s_index -= 1
                else:
                    break
            while t_index >= 0:
                if T[t_index] == "#":
                    t_index -= 1
                    t_skip += 1
                elif t_skip > 0:
                    t_skip -= 1
                    t_index -= 1
                else:
                    break
            # 索引都 >= 0
            if t_index >= 0 and s_index >= 0:
                # 当前位置字符不相等 直接返回false
                if T[t_index] != S[s_index]:
                    return False
            else:
                # 两个字符串处理完 长度不等 直接返回false
                if s_index >= 0 or t_index >= 0:
                    return False
            t_index -= 1
            s_index -= 1
        return True

a = Solution().backspaceCompare("ab#c", "ad#c")
b = Solution().backspaceCompare("ab##", "c#d#")
c = Solution().backspaceCompare("a##c","#a#c")
d = Solution().backspaceCompare("a","a#c")
print(a)
print(b)
print(c)
print(d)