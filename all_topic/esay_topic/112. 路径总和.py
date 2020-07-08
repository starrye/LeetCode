#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 112. 路径总和.py
@time: 2020/7/7 09:39
@desc: 
"""
from typing import List
"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     if root is None:
    #         return False
    #     result = self.dfs(root, sum, root.val)
    #     return result
    # def dfs(self, root, sum, current_sum):
    #     if current_sum == sum and root.left is None and root.right is None:
    #         return True
    #     left_flag = False
    #     right_flag = False
    #     if root.left is not None:
    #         left_flag = self.dfs(root.left, sum, current_sum+root.left.val)
    #     if root.right is not None:
    #         right_flag = self.dfs(root.right, sum, current_sum+root.right.val)
    #     return left_flag or right_flag

        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)