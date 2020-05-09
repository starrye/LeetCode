#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 653. 两数之和 IV - 输入 BST.py
@time: 2020/5/9 10:11
@desc: 
"""
from typing import List

"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        from collections import deque
        queue = deque()
        queue.append(root)
        search = set()
        while queue:
            next_layer = []
            while queue:
                cur_num = queue.popleft()
                if cur_num.val in search:
                    return True
                search.add(k - cur_num.val)
                if cur_num.left is not None:
                    next_layer.append(cur_num.left)
                if cur_num.right is not None:
                    next_layer.append(cur_num.right)
            queue = deque(next_layer)
        return False

