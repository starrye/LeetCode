# encoding: utf-8
"""
@author: liuwz
@time: 2021/5/8 10:39 上午
@file: 783. 二叉搜索树节点最小距离.py
@desc: 
"""

from typing import List
"""
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同


示例 1：

输入：root = [4,2,6,1,3]
输出：1
示例 2：

输入：root = [1,0,48,null,null,12,49]
输出：1
 
提示：
树中节点数目在范围 [2, 100] 内
0 <= Node.val <= 105
差值是一个正数，其数值等于两值之差的绝对值
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans = float("+inf")
        self.pre = float("+inf")
        self.help(root)
        return self.ans

    def help(self, root):
        if not root:
            return

        self.help(root.left)
        # 中序遍历处理流程
        # 最小差值一定存在于相邻的结点 因为是BTS
        if root.val != self.pre:
            self.ans = min(self.ans, abs(root.val-self.pre))
        self.pre = root.val

        self.help(root.right)
