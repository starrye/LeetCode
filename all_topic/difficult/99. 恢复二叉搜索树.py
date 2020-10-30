#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 99. 恢复二叉搜索树.py
@time: 2020/10/28 15:12
@desc: 
"""
from typing import List
"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # def help(node, min_, max_):
        #     if not node:
        #         return True
        #     if node.val <= min_ or node.val >= max_:
        #         return False
        #     return help(node.left, min_, node.val) and help(node.right, node.val, max_)
        #
        # return help(root, float('-inf'), float('inf'))

        # 中序遍历
        # 两种情况
        # 1:两个需要交换的元素挨着
        # 只会出现1次 当前元素小于上一个元素的值
        # 第一元素就是first(pre)，第二元素就是curr(当前元素)即为second(第二元素)
        # 那么需要交换的就是当前元素second与上一个元素first的值

        # 2:两个需要交换的元素不挨着
        # 会出现2次 当前元素小于上一个元素的值
        # first记录需要交换的第一个值 也就是pre
        # second记录需要交换的第二个值 也就是curr

        self.pre = None
        self.first = None
        self.second = None
        def help(node):
            if not node:
                return
            help(node.left)
            if self.pre and node.val <= self.pre.val:
                # 第一次遇到当前元素小于上一个元素的情况
                # 记录第一个需要被交换的值
                if not self.first:
                    self.first = self.pre
                # 记录第二个需要被交换的值
                self.second = node
            self.pre = node
            help(node.right)

        help(root)
        self.first.val, self.second.val = self.second.val, self.first.val

