# encoding: utf-8
"""
@Project ：
@File: 剑指 Offer 50. 第一个只出现一次的字符.py
@Author: liuwz
@time: 2022/1/2 6:36 下午
@desc: 
"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dict_ = collections.defaultdict(int)
        for i in s:
            dict_[i] += 1
        for i in dict_:
            if dict_[i] == 1:
                return i
        return " "