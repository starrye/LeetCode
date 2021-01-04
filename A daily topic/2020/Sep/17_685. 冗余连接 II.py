#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 685. 冗余连接 II.py
@time: 2020/9/17 10:12
@desc: 
"""
from collections import defaultdict
from typing import List
"""
在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
示例 1:

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的有向图如下:
  1
 / \
v   v
2-->3
示例 2:

输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
输出: [4,1]
解释: 给定的有向图如下:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
注意:

二维数组大小的在3到1000范围内。
二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。
"""

"""
1。父亲冲突节点-删除在环上的父亲的边
2。存在环 - 删除环的最后一条边
"""
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        relations = defaultdict(list)

        # 判断p是否是c的祖先节点
        def get_p(p, c):
            if p in relations[c]:
                return True
            if not relations[c]:
                return False
            return get_p(p, relations[c][0])
        # 两个父亲冲突节点
        conf = []
        # 环节点
        recu = []

        for p, c in edges:
            if relations[c]:
                conf.append([relations[c][0], c])
                conf.append([p, c])
            # 注意这里的调用函数get_p(c, p)参数 目的是判断子节点是否是父节点的祖先节点 也就是是否有环
            elif not recu and get_p(c, p):
                recu.append([p, c])
            relations[c].append(p)
        # 父节点冲突
        # 删除在环上的父节点。如何判断父节点在不在环上 那就是判断子节点是不是父节点的祖先节点
        if conf:
            # conf[0][1]是冲突节点子节点 [0][0]是冲突父节点
            if get_p(conf[0][1], conf[0][0]):
                return conf[0]
            else:
                return conf[1]

        # 存在循环节点
        if recu:
            return recu[-1]

a = Solution().findRedundantDirectedConnection([[1,2],[1,3],[2,3]])
print(a)