#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 98. 验证二叉搜索树.py
@time: 2020/8/20 16:59
@desc: 
"""
from typing import List
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # def help(node, min_, max_):
        #     if not node:
        #         return True
        #     if node.val <= min_ or node.val >= max_:
        #         return False
        #     return help(node.left, min_, node.val) and help(node.right, node.val, max_)
        #
        # return help(root, float('-inf'), float('inf'))

        # 中序遍历
        self.pre = float('-inf')
        def help(node):
            if not node:
                return True
            if not help(node.left):
                return False
            if node.val <= self.pre:
                return False
            self.pre = node.val
            return help(node.right)

        return help(root)

