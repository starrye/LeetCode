#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 并查集模版.py
@time: 2020/6/8 10:45
@desc: 
"""
from typing import List


class UF:
    parent = {}
    # equations 表示 关系 实例 ["a==b","c==d"]
    def __init__(self, equations):
        for eq in equations:
            self.parent[eq[0]] = eq[0]
            self.parent[eq[3]] = eq[3]

    # 任意节点找根节点 根节点的父节点是自己
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    # 合并两个集合
    def union(self, p, q):
        # 如果两个集合本身就在同一个根节点下则返回
        if self.connected(p, q): return
        # p的根节点变成q的根节点的子节点
        self.parent[self.find(p)] = self.find(q)

    def connected(self, p, q):
        return self.find(p) == self.find(q)
