#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 538. 把二叉搜索树转换为累加树.py
@time: 2020/9/21 10:31
@desc: 
"""
from typing import List
"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

 

例如：

输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:return []
        stack = [(root, 1)]
        sum = 0
        while stack:
            node, flag = stack.pop()
            if not flag:
                sum += node.val
                node.val = sum
                continue
            if node.left:
                stack.append((node.left, 1))
            stack.append((node, 0))
            if node.right:
                stack.append((node.right, 1))
        return root
