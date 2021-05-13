# encoding: utf-8
"""
@author: liuwz
@time: 2021/5/10 3:00 下午
@file: 99. 恢复二叉搜索树.py
@desc: 
"""

from typing import List
"""
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

示例 1：

输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
示例 2：


输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。

提示：

树上节点的数目在范围 [2, 1000] 内
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre = None
        self.first = None
        self.second = None

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.midOrder(root)
        # 交换结点值
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

    # 中序遍历
    def midOrder(self, root):
        if not root:
            return
        self.midOrder(root.left)
        self.check_node(root)
        self.midOrder(root.right)

    # 检查相邻结点是否位置错误
    def check_node(self, root):
        if self.pre and root.val < self.pre.val:
            # 记录第一个结点
            if not self.first:
                self.first = self.pre
            # 更新第二个结点 这里不能用else 因为两个结点可能是相邻的 比如1 3 2 4 如果使用else 则只能记录first = 3
            self.second = root
        self.pre = root