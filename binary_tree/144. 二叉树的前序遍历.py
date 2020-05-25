#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 144. 二叉树的前序遍历.py
@time: 2020/5/22 15:16
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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, result = [root], []
        while stack:
            current_node = stack.pop()
            if isinstance(current_node, TreeNode):
                stack.extend([current_node.right, current_node.left,current_node.val])
            elif isinstance(current_node, int):
                result.append(current_node)
        return result