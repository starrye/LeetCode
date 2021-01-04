#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 102. 二叉树的层序遍历.py
@time: 2020/5/13 14:01
@desc: 
"""
from typing import List
"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            current_layer_list = []
            next_layer = []
            while queue:
                current_layer_elm = queue.popleft()
                current_layer_list.append(current_layer_elm.val)
                if current_layer_elm.left is not None:
                    next_layer.append(current_layer_elm.left)
                if current_layer_elm.right is not None:
                    next_layer.append(current_layer_elm.right)
            result.append(current_layer_list)
            queue = deque(next_layer)
        return result