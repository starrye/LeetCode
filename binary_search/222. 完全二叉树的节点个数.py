#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 222. 完全二叉树的节点个数.py
@time: 2020/11/24 09:51
@desc: 
"""
from collections import deque
from typing import List
"""
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入: 
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # queue = deque()
        # queue.append(root)
        # layer = -1
        # while queue:
        #     next_layer = []
        #     current_node = 0
        #     layer += 1
        #     while queue:
        #         node = queue.popleft()
        #         current_node += 1
        #         if node.left:
        #             next_layer.append(node.left)
        #         if node.right:
        #             next_layer.append(node.right)
        #     if (current_node != (2 ** layer)) or not next_layer:
        #         return 2 ** layer - 1 + current_node
        #     queue = deque(next_layer)


        # 二分法查到存在的最右侧节点 也就是有多少叶子节点 然后 加上 2 ** layer - 1
        if not root:
            return 0
        d = self.countDepth(root)
        if d == 0:
            return 1
        left, right = 0, 2 ** d -1
        while left <= right:
            mid = left + (right - left) //2
            if self.exist(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1
        return left + 2 ** d - 1

    def exist(self, id, d, node):
        left, right = 0, 2 ** d - 1
        for i in range(d):
            mid = left + (right - left) // 2
            if id <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid
        return node is not None

    def countDepth(self, root):
        d = 0
        while root.left:
            root = root.left
            d += 1
        return d

