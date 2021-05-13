#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 144. 二叉树的前序遍历.py
@time: 2020/10/27 10:19
@desc: 
"""
from typing import List
"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        # 递归
        def help(root):
            if root:
                stack.append(root.val)
                help(root.left)
                help(root.right)
        stack = list()
        help(root)
        return stack

        # 迭代
        # if not root:
        #     return
        # stack = [root]
        # result = []
        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return result