# encoding: utf-8
"""
@author: liuwz
@time: 2021/3/29 2:04 下午
@file: 103. 二叉树的锯齿形层序遍历.py
@desc: 
"""
from collections import deque

"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        flag = 0  # 0:左到右 1:右到左
        while queue:
            next_layer = []
            current_val = []
            while queue:
                node = queue.popleft()
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
                if not flag:
                    current_val.append(node.val)
                else:
                    current_val.insert(0, node.val)

            ans.append(current_val)
            queue = deque(next_layer)
            flag = not flag
        return ans

