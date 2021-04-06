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
        """

        :param root:
        :return:
        """
        # 1 边界条件
        if not root:
            return []
        result = []
        from collections import deque
        queue = deque()
        # 2 初始化队列
        queue.append(root)
        while queue:
            # 3 获取当前层里面元素的个数
            qsize = len(queue)
            # 4 当前层的结果存放于列表中
            current_layer_list = []
            # 5 遍历当前层的每个节点
            while qsize:
                current_layer_elm = queue.popleft()
                qsize -= 1
                # 6 结果存放到当前层中
                current_layer_list.append(current_layer_elm.val)
                # 7 把下一层的结点入队，需满足非空
                if current_layer_elm.left is not None:
                    queue.append(current_layer_elm.left)
                if current_layer_elm.right is not None:
                    queue.append(current_layer_elm.right)
            result.append(current_layer_list)
        return result