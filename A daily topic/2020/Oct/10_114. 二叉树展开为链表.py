#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 114. 二叉树展开为链表.py
@time: 2020/10/27 16:18
@desc: 
"""
from typing import List
"""
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # last = None
        # def help(root):
        #     if not root:
        #         return
        #     help(root.right)
        #     help(root.left)
        #     nonlocal last
        #     root.right = last
        #     root.left = None
        #     last = root
        # help(root)

        # 右节点挂到左节点的最右节点的右节点
        # 左节点放到右节点
        # 左节点置为空
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left and root.right:
            # 找到左节点的最右节点
            left_right = root.left
            while left_right.right:
                left_right = left_right.right
            # 右节点挂到左节点的最右节点的右节点
            left_right.right = root.right
            # 左节点放到右节点
            root.right = root.left
            # 左节点置空
            root.left = None
        # 只有左节点 没有右节点 直接把左节点挂到右节点
        elif not root.right and root.left:
            root.right = root.left
            root.left = None


