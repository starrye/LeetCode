#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 111. 二叉树的最小深度.py
@time: 2020/8/21 09:07
@desc: 
"""
from collections import deque
from typing import List
"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # BFS
        # if not root:
        #     return 0
        # queue = deque()
        # queue.append(root)
        # ans = 0
        # while queue:
        #     ans += 1
        #     next_layer = []
        #     flag = False
        #     while queue:
        #         cur = queue.popleft()
        #         if not (cur.left or cur.right):
        #             flag = True
        #             break
        #         if cur.left:
        #             next_layer.append(cur.left)
        #         if cur.right:
        #             next_layer.append(cur.right)
        #     if flag:
        #         break
        #     queue = deque(next_layer)
        # return ans

        # DFS
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return max(self.minDepth(root.right), self.minDepth(root.left)) + 1