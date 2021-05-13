# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/25 9:59 上午
@file: 113. 路径总和 II.py
@desc: 
"""

from typing import List
"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。

示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
示例 2：
输入：root = [1,2,3], targetSum = 5
输出：[]
示例 3：

输入：root = [1,2], targetSum = 0
输出：[]
 

提示：

树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """
        回溯思想的二叉树前序遍历
        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return []
        ans = []

        def help(root, target, temp):
            if not root:
                return
            # 题目要求根结点到叶子结点
            if not root.left and not root.right:
                # 本层并未对root处理 所以需要判断当前target是否与root相等
                if target == root.val:
                    ans.append(temp + [root.val])
                    return
            # 未到叶子结点
            else:
                # 注意这里的处理 在 传数据的时候进行计算 回溯的时候就会自动回到计算前的状态 因此不需要像用stack存储时需要pop
                # temp存储当前路径
                help(root.left, target - root.val, temp + [root.val])
                help(root.right, target - root.val, temp + [root.val])

        help(root, targetSum, [])
        return ans

print(4/2==2.0)
print(5/3)