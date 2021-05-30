# encoding: utf-8
"""
@author: liuwz
@time: 2021/5/14 5:04 下午
@file: 547.省份数量.py
@desc: 
"""

from typing import List
"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。

示例 1：


输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
示例 2：


输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
 

提示：

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""


class UF(object):
    def __init__(self, n: int):
        self.parent = {}
        self.Cnt = {}
        self.count = 0
        for i in range(n):
            self.parent[i] = i
            self.Cnt[i] = 1
        self.count = n

    def find_par(self, x):
        if x == self.parent[x]:
            return x
        # 路径压缩
        self.parent[x] = self.find_par(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_par = self.find_par(x)
        y_par = self.find_par(y)
        if x_par != y_par:
            self.parent[x_par] = y_par
            self.Cnt[y_par] += 1
            self.count -= 1

    def size(self, x):
        return self.Cnt[self.find_par(x)]

    def Count(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_count = len(isConnected)
        uf = UF(city_count)
        for index, relation in enumerate(isConnected):
            for i, v in enumerate(relation):
                if i != index:
                    if v == 1:
                        uf.union(index, i)
        return uf.Count()


a = Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
print(a)