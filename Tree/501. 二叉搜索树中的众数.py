#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 501. 二叉搜索树中的众数.py
@time: 2020/9/24 09:52
@desc: 
"""
from collections import Counter
from typing import List
"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def findMode(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     self.root_list = []
    #     self.dfs(root)
    #
    #
    # def dfs(self, root):
    #     if not root:
    #         return
    #     self.dfs(root.left)
    #     self.root_list.append(root.val)
    #     self.dfs(root.right)

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.max = -1
        self.pre = float("+inf")
        self.pre_count = 0
        self.ans = []
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        # 发现当前数与上一个数字相等 结果+1
        if self.pre == root.val:
            self.pre_count += 1
        # 当前数字与上一个数字不等 重制1
        else:
            self.pre_count = 1
        # 发现数量更多的数 清除旧的列表 重新添加
        if self.pre_count > self.max:
            self.ans = []
            self.ans.append(root.val)
            self.max = self.pre_count
        # 发现数量相当的数 添加当前数字
        elif self.pre_count == self.max:
            self.ans.append(root.val)
        self.pre = root.val
        self.dfs(root.right)
