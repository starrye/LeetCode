#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 257. 二叉树的所有路径.py
@time: 2020/9/4 09:40
@desc: 
"""
from typing import List

"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []
        def dfs(root, path):
            if root.left is None and root.right is None:
                path += str(root.val)
                ans.append(path)
                return
            path += str(root.val) + "->"
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)

        dfs(root, "")
        return ans
