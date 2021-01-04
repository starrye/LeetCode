#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 968. 监控二叉树.py
@time: 2020/9/22 10:29
@desc: 
"""
from typing import List
"""
给定一个二叉树，我们在树的节点上安装摄像头。
节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
计算监控树的所有节点所需的最小摄像头数量。

示例 1：

输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。
示例 2：



输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：

给定树的节点数的范围是 [1, 1000]。
每个节点的值都是 0。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.camera = 0
        self.dfs(root)
        return self.camera + int(root.val == 1)

    # root.val = 1: 叶子节点
    # root.val = 0: 左孩子或者右孩子有监控
    # root.val = 2: 本节点部署监控
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if not left and not right:
            root.val = 1
        elif left == 1 or right == 1:
            self.camera += 1
            root.val = 2
        else:
            root.val = 0
        return root.val

