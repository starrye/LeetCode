#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 767. 重构字符串.py
@time: 2020/11/30 11:11
@desc: 
"""
import heapq
from collections import Counter
from typing import List

"""
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        if n == 1:
            return S
        s_num = Counter(S)
        if max(s_num.values()) > (n + 1) // 2:
            return ""

        result = ""
        # 添加字母
        pq = []
        for s, c in s_num.items():
            heapq.heappush(pq, (-c, s))
        prev = (0, None)

        # 这里值变为负数 因为heapq只实现了小顶堆 所有-c 最小即为最大
        # 每次把数量最多的字母加入结果
        # 然后把他从堆中去掉 数量-1
        # 然后加入上一个去掉的字母
        while pq:
            v, k = heapq.heappop(pq)
            result += k
            if prev[0] < 0:
                heapq.heappush(pq, prev)
            prev = (v + 1, k)
        return result

a = Solution().reorganizeString("ab")
print(a)

