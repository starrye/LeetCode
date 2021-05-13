# encoding: utf-8
"""
@author: liuwz
@time: 2021/5/10 6:25 下午
@file: 701. 二叉搜索树中的插入操作.py
@desc: 
"""

from typing import List
"""
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。
注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。

示例 1：
输入：root = [4,2,7,1,3], val = 5
输出：[4,2,7,1,3,5]
解释：另一个满足题目要求可以通过的树是：

示例 2：
输入：root = [40,20,60,10,30,50,70], val = 25
输出：[40,20,60,10,30,50,70,null,null,25]
示例 3：

输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
输出：[4,2,7,1,3,5]

提示：
给定的树上的节点数介于 0 和 10^4 之间
每个节点都有一个唯一整数值，取值范围从 0 到 10^8
-10^8 <= val <= 10^8
新值和原始二叉搜索树中的任意节点值都不同
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 如果是空树 直接插入
        if not root:
            return TreeNode(val)

        # 如果当年结点的值大于要插入的值
        if root.val > val:
            # 如果当前结点有左子树 则递归左子树
            if root.left:
                self.insertIntoBST(root.left, val)
            # 当前结点没有左子树 则插入为当前结点的左子树
            else:
                root.left = TreeNode(val)

        # 如果当年结点的值小于要插入的值
        elif root.val < val:
            # 如果当前结点有右子树 则递归右子树
            if root.right:
                self.insertIntoBST(root.right, val)
            # 当前结点没有右子树 则插入为当前结点的右子树
            else:
                root.right = TreeNode(val)
        return root