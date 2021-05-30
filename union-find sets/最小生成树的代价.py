# encoding: utf-8
"""
@author: liuwz
@time: 2021/5/26 11:01 上午
@file: 最小生成树的代价.py
@desc: 
"""

from typing import List
"""
给定点集和边集，求最小生成树的代价，如果最后不能生成最小生成树，那么返回MAX_INT。

输入：N = 2， conn = [[1, 2, 37], [2, 1, 17], [1, 2, 68]]
输出：17
解释：图中只有两个点 [1, 2]，当然是选择最小连接 [2, 1, 17]
"""

class UF:
    def __init__(self, n):
        self.par = {}
        self.Cnt = {}
        for i in range(1, n+1):
            self.par[i] = i
            self.Cnt[i] = 1
        self.size = n

    def find(self, x):
        if x == self.par[x]:
            return x

        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x_par = self.par[x]
        y_par = self.par[y]
        if x_par != y_par:
            self.par[x_par] = y_par
            self.Cnt[y_par] += self.Cnt[x_par]
            self.size -= 1
            return True
        return False


class MST:
    def solve(self, N, conn):
        ans = 0
        uf = UF(N)
        conn_new = sorted(conn, key=lambda x: x[2])
        for con in conn_new:
            res = uf.union(con[0], con[1])
            if res:
                ans += con[2]

        for e in conn:
            if uf.find(e[0]) != uf.find(e[1]):
                return -1
        return ans


a = MST().solve(3, [[3, 1, 37], [2, 1, 17], [1, 3, 68]])
print(a)