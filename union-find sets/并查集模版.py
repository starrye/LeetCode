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
    def __init__(self, n):
        # 集合关系
        self.parent = {}
        # 每个集合内数量
        self.Cnt = {}
        for i in range(n):
            self.parent[i] = i
            self.Cnt[i] = 1
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
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 合并两个集合
    def union(self, x, y):
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
