# encoding: utf-8
"""
@Project ：
@File: 208. 实现 Trie (前缀树) 难度 中等  1205.py
@Author: liuwz
@time: 2022/6/18 17:55
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
 

提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次
"""

# 1/利用字典k,v依次存储当前字符与下一个字符的关系
# 2/利用#作为叶子结点表示当前字符的结束，此条路径便可组成一个完成的字符串
# 3/判断前缀 与判断字符串是否存在的区别在于 前者判断# 后者查找完直接返回True即可


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur["#"] = "#"

    def search(self, word: str) -> bool:
        cur = self.trie
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        return "#" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)