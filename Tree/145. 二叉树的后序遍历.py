#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 145. 二叉树的后序遍历.py
@time: 2020/9/29 09:26
@desc: 
"""
from typing import List
"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # result = []
        # def help(root):
        #     if not root:
        #         return
        #     help(root.left)
        #     help(root.right)
        #     result.append(root.val)
        # help(root)
        # return result

        # 迭代
        if not root:
            return
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.val, node.right, node.left])
            if isinstance(node, int):
                result.append(node)
        return result











