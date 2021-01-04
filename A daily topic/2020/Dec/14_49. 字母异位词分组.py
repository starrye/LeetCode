#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 49. 字母异位词分组.py
@time: 2020/12/14 10:32
@desc: 
"""
from typing import List
"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in dict_:
                dict_[key] = [i]
            else:
                dict_[key].append(i)
        return list(dict_.values())


a = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(a)