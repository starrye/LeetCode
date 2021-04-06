# encoding: utf-8
"""
@author: liuwz
@time: 2021/3/31 5:53 下午
@file: 107. 二叉树的层序遍历 II.py
@desc: 
"""
"""
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            current_layer_list = []
            next_layer = []
            while queue:
                current_layer_elm = queue.popleft()
                current_layer_list.append(current_layer_elm.val)
                if current_layer_elm.left is not None:
                    next_layer.append(current_layer_elm.left)
                if current_layer_elm.right is not None:
                    next_layer.append(current_layer_elm.right)
            result.insert(0, current_layer_list)
            queue = deque(next_layer)
        return result