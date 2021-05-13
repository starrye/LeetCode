# encoding: utf-8
"""
@author: liuwz
@time: 2021/5/10 6:00 下午
@file: 450. 删除二叉搜索树中的节点.py
@desc: 
"""

from typing import List
"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        # 如果当前结点比目标结点值小 则往右子树寻找
        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        # 如果当前结点比目标结点值大 则往左子树寻找
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        # 当前结点为目标结点
        else:
            # 如果当前结点为叶子结点 则返回None
            if (not root.right) and (not root.left):
                return None

            # 如果当前结点有左子树
            elif root.left:
                node = root.left
                # 找到左子树的最右侧结点 即跟当前结点最接近的结点 也是可以替换当前结点的结点
                while node.right:
                    node = node.right
                # 这里只是更换值 目的是把要替换的结点放到叶子结点 才能删除
                root.val, node.val = node.val, root.val
                root.left = self.deleteNode(root.left, key)

            # 如果当前结点有右子树(这里与上述先判断左子树逻辑可以互换 因为 左子树的最右侧结点  当前结点 右子树的最左侧结点 是相邻的)
            elif root.right:
                node = root.right
                # 找到右子树的最左侧结点 即跟当前结点最接近的结点 也是可以替换当前结点的结点
                while node.left:
                    node = node.left
                root.val, node.val = node.val, root.val
                root.right = self.deleteNode(root.right, key)

        return root