# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/1 11:31 上午
@file: 1302. 层数最深叶子节点的和.py
@desc: 
"""
from collections import deque

"""
给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。
示例 1：


输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
示例 2：

输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：19
 

提示：

树中节点数目在范围 [1, 104] 之间。
1 <= Node.val <= 100
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        queue = deque()
        queue.append(root)
        while queue:
            qsize = len(queue)
            current_sum = 0
            while qsize:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                qsize -= 1
                current_sum += node.val
            ans = current_sum
        return ans
