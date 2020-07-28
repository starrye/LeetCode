#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 104. 二叉树的最大深度.py
@time: 2020/7/28 09:27
@desc: 
"""
from collections import deque
from typing import List
"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # dfs
        # if not root:
        #     return 0
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)
        # return max(left, right) + 1

        # bfs
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            # 保存下一层所有节点
            next_layer = []
            while queue:
                node = queue.popleft()
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            queue = deque(next_layer)
        return depth