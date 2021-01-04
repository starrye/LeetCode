#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 106. 从中序与后序遍历序列构造二叉树.py
@time: 2020/9/25 09:37
@desc: 
"""
from typing import List
"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 直接递归
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return root

    # 索引对应存储字典 减少寻找索引操作
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    #     index_dict = {}
    #     for index, value in enumerate(inorder):
    #         index_dict[value] = index
    #     length = len(inorder)
    #     def help(inorder_b, inorder_e, postorder_b, postorder_e):
    #         if inorder_b == inorder_e:
    #             return
    #         root = TreeNode(postorder[postorder_e - 1])
    #         index = index_dict[postorder[postorder_e - 1]]
    #         root.left = help(inorder_b, index, postorder_b, postorder_b + index - inorder_b)
    #         root.right = help(index + 1, inorder_e, postorder_b + index - inorder_b, postorder_e - 1)
    #         return root
    #
    #     return help(0, length, 0, length)