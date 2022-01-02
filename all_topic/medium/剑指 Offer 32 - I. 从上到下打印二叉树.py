# encoding: utf-8
"""
@Project ：
@File: 剑指 Offer 32 - I. 从上到下打印二叉树.py
@Author: liuwz
@time: 2022/1/2 6:43 下午
@desc: 
"""
from collections import deque

"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        Q = deque([root])
        result = []
        while Q:
            current_layer = []
            while Q:
                node = Q.popleft()
                result.append(node.val)
                if node.left:
                    current_layer.append(node.left)
                if node.right:
                    current_layer.append(node.right)
            Q = deque(current_layer)
        return result