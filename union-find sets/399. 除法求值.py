# encoding: utf-8
"""
@author: liuwz
@time: 2021/5/20 11:33 上午
@file: 399. 除法求值.py
@desc: 
"""

from typing import List
"""
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。
注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

 

示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
 

提示：

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj 由小写英文字母与数字组成
"""


class UF:
    def __init__(self, n):
        # 集合关系
        self.parent = {}
        # 比例关系
        self.rate = {}
        for i in range(n):
            self.parent[i] = i
            self.rate[i] = 1.0
        # 集合数量
        self.count = n

    # 任意节点找根节点 根节点的父节点是自己
    def find(self, x):
        # 路径压缩 简单来说就是 把糖葫芦造型的数据 改成 一把扇子 每一扇叶都直接和扇柄相连
        if x == self.parent[x]:
            return x
        # 此过程把当前节点指向根节点 等于做了完全压缩
        # 比如 1->3->4->5 在此过程 把1的父节点更新为(把3的父节点更新为(找到4的根节点5)->5)->5
        # 其实就是从最底层更新时采用递归 在递归过程中顺便把父节点也更新为根节点  ！！！因为最终递归的出口是根节点


    # 合并两个集合
    def union(self, x, y, rate):
        x_parent = self.find(x)
        y_parent = self.find(y)
        # 如果两个集合本身就在同一个根节点下则返回
        if x_parent == y_parent:
            return
        # x的根节点变成y的根节点的子节点
        self.parent[x_parent] = y_parent
        self.Cnt[y_parent] += self.Cnt[x_parent]
        self.count -= 1

    # 返回任意集合的size
    def size(self, x):
        return self.Cnt[self.find(x)]

    # 返回集合数量
    def Count(self):
        return self.count
