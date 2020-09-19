#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 404. 左叶子之和.py
@time: 2020/9/19 10:40
@desc: 
"""
from typing import List
"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0

        def dfs(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                nonlocal result
                result += root.left.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return result