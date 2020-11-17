#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1657. 确定两个字符串是否接近.py
@time: 2020/11/16 09:57
@desc: 
"""
from typing import List
"""
如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：

操作 1：交换任意两个 现有 字符。
例如，abcde -> aecdb
操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。

 

示例 1：

输入：word1 = "abc", word2 = "bca"
输出：true
解释：2 次操作从 word1 获得 word2 。
执行操作 1："abc" -> "acb"
执行操作 1："acb" -> "bca"
示例 2：

输入：word1 = "a", word2 = "aa"
输出：false
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
示例 3：

输入：word1 = "cabbba", word2 = "abbccc"
输出：true
解释：3 次操作从 word1 获得 word2 。
执行操作 1："cabbba" -> "caabbb"
执行操作 2："caabbb" -> "baaccc"
执行操作 2："baaccc" -> "abbccc"
示例 4：

输入：word1 = "cabbba", word2 = "aabbss"
输出：false
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
 

提示：

1 <= word1.length, word2.length <= 105
word1 和 word2 仅包含小写英文字母
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        if len(word1) != len(word2):return False
        w1_r = Counter(word1)
        w2_r = Counter(word2)
        print(w2_r)
        w1_d = sorted(w1_r)
        w2_d = sorted(w2_r)
        w1_v = sorted(w1_r.values())
        w2_v = sorted(w1_r.values())
        print(w1_v)
        print(w2_v)
        print(w1_d)
        print(w2_d)
        return w1_v == w2_v and w1_d == w2_d


a = Solution().closeStrings("abbzzca", "babzzcz")
print(a)