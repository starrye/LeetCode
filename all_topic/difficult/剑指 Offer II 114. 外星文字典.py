# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer II 114. 外星文字典.py
@Author: liuwz
@time: 2022/5/31 11:03 AM
@desc: 
"""
from collections import defaultdict
from itertools import pairwise
from typing import List

"""
现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。

给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。

请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

字符串 s 字典顺序小于 字符串 t 有两种情况：

在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。
 

示例 1：

输入：words = ["wrt","wrf","er","ett","rftt"]
输出："wertf"
示例 2：

输入：words = ["z","x"]
输出："zx"
示例 3：

输入：words = ["z","x","z"]
输出：""
解释：不存在合法字母顺序，因此返回 "" 。
 

提示：

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] 仅由小写英文字母组成
"""

# 拓扑排序
# 1/定义graph=defaultdict(list) d=[]
# 2/graph key为入度 value为出度 d 记录value的入度
# 3/寻找入度为0的点 入队列
# 4/然后寻找对应的出度点 并将其入度-1
# 5/然后继续寻找入度为0的点 入队 (遍历队列 不要出度)
# 6/通过队列的长度 和 原始去重字符串的长度 判断是否相等 进而判断是否有环

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph, s = defaultdict(list), set()
        for w in words:
            s = s.union(set(w))
        d = [0] * 26
        # pairwise(x)    Return an iterator of overlapping pairs taken from the input iterator. ABCD -> AB BC CD
        for a, b in pairwise(words):
            for ca, cb in zip(a, b):
                # 说明ca排在cb之前 拓扑可以变为 ca->cb ca出度+1 cb入度+1
                if ca != cb:
                    graph[ca].append(cb)
                    d[ord(cb) - ord('a')] += 1
                    break
            # 长度不同
            else:
                # abc > ab 这种不符合规则 ab abc 这种无法比较字母的字典序
                if len(a) > len(b):
                    return ""
        start = [k for k in s if d[ord(k) - ord('a')] == 0]
        # 拓扑遍历 依次获取入度为0的点
        for ch in start:
            for nxt in graph[ch]:
                d[v := ord(nxt) - ord('a')] -= 1
                if not d[v]:
                    start.append(nxt)
        return "".join(start) if len(start) == len(s) else ""


a = Solution().alienOrder(["wrt","wrf","er","ett","rftt"])
print(a)