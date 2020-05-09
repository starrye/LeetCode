#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 551.出勤记录.py
@time: 2020/5/6 10:51
@desc: 
"""
from typing import List
"""
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True
示例 2:

输入: "PPALLL"
输出: False
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        return not(s.count("A") > 1 or "LLL" in s)
        # A_count = 0
        # L_continuous_count = 0
        # for i in s:
        #     if i == "L":
        #         if L_continuous_count == 2:
        #             return False
        #         L_continuous_count += 1
        #         continue
        #     elif i == "A":
        #         if A_count:
        #             return False
        #         A_count = 1
        #     L_continuous_count = 0
        # return True

a = Solution().checkRecord("PPALLL")
print(a)




