#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 94. 二叉树的中序遍历.py
@time: 2020/5/14 15:45
@desc: 
"""
from typing import List
"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
"""


from binary_tree.tree import stringToTreeNode
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代
        # stack, res = [root], []
        # while stack:
        #     i = stack.pop()
        #     if isinstance(i, TreeNode):
        #         stack.extend([i.right,i.val,i.left])
        #     elif isinstance(i, int):
        #         res.append(i)
        # return res
        # 递归
        res = self.digui(root, [])
        return res

    def digui(self, root, res):
        if not root:
            return
        self.digui(root.left, res)
        res.append(root.val)
        self.digui(root.right, res)
        return res



root = stringToTreeNode([1,"null",2,3])
a = Solution().inorderTraversal(root)
print(a)
