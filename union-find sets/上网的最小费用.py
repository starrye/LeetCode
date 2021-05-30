# encoding: utf-8
"""
@author: liuwz
@time: 2021/5/26 11:27 上午
@file: 上网的最小费用.py
@desc: 
"""
from typing import List

"""
园区里面有很多大楼，编号从 1~N。第 i 大楼可以自己花钱买路由器上网，费用为 cost[i-1]，也可以从别的大楼拉一根网线来上网，
比如大楼 a 和大楼 b 之间拉网线的费用为 c，表示为一条边 [a, b, c]。输入为每个大楼自己买路由器和拉网线的费用，
请问，让所有大楼都能够上网的最小费用是多少？上网具有联通性，只要与能够上网的大楼连通，即可上网。

输入：cost = [1, 2, 3], edges = [[1,2,100], [2,3,3]]
输出：6
"""


class UF:
    def __init__(self, n):
        self.par = {}
        self.Cnt = {}
        for i in range(n):
            self.par[i] = i
            self.Cnt[i] = 1
        self.size = n

    def find(self, x):
        if x == self.par[x]:
            return x

        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)
        if x_par != y_par:
            self.par[x_par] = y_par
            self.Cnt[y_par] += self.Cnt[x_par]
            self.size -= 1
            return True
        return False

class Solution:
    def minCostToSupplyWater(self, n: int, cost: List[int], es: List[List[int]]):
        uf = UF(n + 1)
        # 加入虚拟点 0 并且0到各个点的花费都是cost数组的值也就是自己拉网线的花费
        for i, v in enumerate(cost):
            es.append([0, i + 1, v])

        # 最小生成树的流程
        es_new = sorted(es, key=lambda x: x[2])
        ans = 0
        for es_ in es_new:
            res = uf.union(es_[0], es_[1])
            if res:
               ans += es_[2]
        return ans


a = Solution().minCostToSupplyWater(3, [1, 2, 3], [[1,2,100], [2,3,6]])
print(a)

