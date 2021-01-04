#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 530. 二叉搜索树的最小绝对差.py
@time: 2020/10/12 10:50
@desc: 
"""
from typing import List
"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：

树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
！！！二叉搜索树的中序遍历 是 递增的有序数组
"""

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans, pre = float("+inf"), float("-inf")
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nonlocal ans, pre
            ans = min(ans, root.val - pre)
            pre = root.val
            dfs(root.right)
        dfs(root)
        return ans
