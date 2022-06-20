# encoding: utf-8
"""
@Project ：
@File: 677. 键值映射.py
@Author: liuwz
@time: 2022/6/20 23:27
@desc: 
"""
from collections import deque

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
"""
设计一个 map ，满足以下几点:

字符串表示键，整数表示值
返回具有前缀等于给定字符串的键的值的总和
实现一个 MapSum 类：

MapSum() 初始化 MapSum 对象
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对 key-value 将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
 

示例 1：

输入：
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]

解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // 返回 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // 返回 5 (apple + app = 3 + 2 = 5)
 

提示：

1 <= key.length, prefix.length <= 50
key 和 prefix 仅由小写英文字母组成
1 <= val <= 1000
最多调用 50 次 insert 和 sum

"""

# 1/注意如果单词已经存在的话 需要替换val 所以在最后存储val
# 2/dfs或者bfs 统计当前位置的总和

class MapSum:

    def __init__(self):
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.trie
        for w in key:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur["#"] = val

    def sum(self, prefix: str) -> int:
        cur = self.trie
        for w in prefix:
            if w not in cur:
                return 0
            cur = cur[w]
        return self.dfs(cur)

    def dfs(self, node):
        ans = 0
        for n in node:
            if "#" == n:
                ans += node["#"]
            else:
                ans += self.dfs(node[n])
        return ans

    def bfs(self, node):
        ans = 0
        q = deque([node])
        while q:
            n = q.popleft()
            for k, v in n.items():
                if "#" == k:
                    ans += n["#"]
                else:
                    q.append(v)
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)