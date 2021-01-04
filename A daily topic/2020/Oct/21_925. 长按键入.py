#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 925. 长按键入.py
@time: 2020/10/21 09:18
@desc: 
"""
from collections import Counter, defaultdict
from typing import List
"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：

输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：

输入：name = "leelee", typed = "lleeelee"
输出：true
示例 4：

输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。
 

提示：

name.length <= 1000
typed.length <= 1000
name 和 typed 的字符都是小写字母。
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # if name == typed:
        #     return True
        # n_length = len(name)
        # t_length = len(typed)
        # i, j = 0, 0
        # while i < n_length and j < t_length:
        #     if i == 0:
        #         if name[i] != typed[j]:
        #             return False
        #     else:
        #         if typed[j] != name[i]:
        #             if typed[j] != typed[j-1]:
        #                 return False
        #             else:
        #                 j += 1
        #                 continue
        #     if i == n_length and len(set(typed[j:])) != 1:
        #         return False
        #     i += 1
        #     j += 1
        # return i == n_length

        i, j = 0, 0
        while j < len(typed):
            # 两个串当前位置字符相等
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            # 如果name[i - 1] == typed[j] 说明 typed在重复打字 直接往后+1 再与name做比较
            elif j > 0 and typed[j] == name[i - 1]:
                j += 1
            else:
                return False
        return i == len(name)



a = Solution().isLongPressedName("alex", "aaleexxx")
b = Solution().isLongPressedName("saeed", "ssaaedd")
c = Solution().isLongPressedName("a", "aa")
d = Solution().isLongPressedName("pyplrz", "ppyypllr")

print(a)
print(b)
print(c)
print(d)