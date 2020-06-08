#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 990. 等式方程的可满足性.py
@time: 2020/6/8 10:42
@desc: 
"""
from typing import List
"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 
示例 1：
输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
示例 2：

输出：["b==a","a==b"]
输入：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
示例 3：

输入：["a==b","b==c","a==c"]
输出：true
示例 4：

输入：["a==b","b!=c","c==a"]
输出：false
示例 5：

输入：["c==c","b==d","x!=z"]
输出：true
 

提示：

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] 和 equations[i][3] 是小写字母
equations[i][1] 要么是 '='，要么是 '!'
equations[i][2] 是 '='
"""
class UF:
    parent = {}
    # equations 表示 关系 实例 ["a==b","c==d"]
    def __init__(self, equations):
        for eq in equations:
            self.parent[eq[0]] = eq[0]
            self.parent[eq[3]] = eq[3]

    # 任意节点找根节点 根节点的父节点是自己
    def find(self, x):
        # 没有路径压缩
        # while x != self.parent[x]:
        #     x = self.parent[x]
        # return x

        # 路径压缩
        if x == self.parent[x]:
            return x
        # 此过程把当前节点指向根节点 等于做了完全压缩
        # 比如 1->3->4->5 在此过程 把1的父节点更新为(把3的父节点更新为(找到4的根节点5)->5)->5
        # 其实就是从最底层更新时采用递归 在递归过程中顺便把父节点也更新为根节点  ！！！因为最终递归的出口是根节点
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 合并两个集合
    def union(self, p, q):
        # 如果两个集合本身就在同一个根节点下则返回
        if self.connected(p, q): return
        # p的根节点变成q的根节点的子节点
        self.parent[self.find(p)] = self.find(q)

    def connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(equations)

        for eq in equations:
            if eq[1] == "=":
                uf.union(eq[0], eq[-1])
        print(uf.parent)
        for eq in equations:
            if eq[1] == "!" and uf.connected(eq[0], eq[3]):
                return False
        return True


a = Solution().equationsPossible(["a==b","b==c","a==c"])