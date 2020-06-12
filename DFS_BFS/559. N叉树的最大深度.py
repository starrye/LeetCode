#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 559. N叉树的最大深度.py
@time: 2020/6/10 11:25
@desc: 
"""
from typing import List
"""
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :

 

我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。
树的节点总不会超过 5000。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        from collections import deque
        queue_ = deque()
        queue_.append(root)
        result = 0
        while queue_:
            result += 1
            next_layer = []
            while queue_:
                node = queue_.popleft()
                if node.children:
                    next_layer.append(node.children)
            if next_layer:
                for i in next_layer:
                    for j in i:
                        queue_.append(j)
        return result