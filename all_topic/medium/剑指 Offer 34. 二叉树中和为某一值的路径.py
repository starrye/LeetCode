# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 34. 二叉树中和为某一值的路径.py
@Author: liuwz
@time: 2022/1/11 10:10 上午
@desc: 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:return []
        result = []
        def dfs(root, target, ans):
            if not root.left and not root.right and target == root.val:
                result.append(ans + [root.val])
                return
            if root.left:
                dfs(root.left, target-root.val, ans+[root.val])
            if root.right:
                dfs(root.right, target-root.val, ans+[root.val])
        dfs(root, target, [])
        return result