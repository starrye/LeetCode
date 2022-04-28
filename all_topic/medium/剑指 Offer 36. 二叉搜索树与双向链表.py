# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 36. 二叉搜索树与双向链表.py
@Author: liuwz
@time: 2022/1/11 11:07 上午
@desc: 
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        pre, head = None, None
        def dfs(root):
            if not root:
                return
            dfs(root.left)

            nonlocal pre, head
            # 中序遍历
            if not pre:
                # 此时root是最左侧叶子节点 也就是最小节点
                head = root
            else:
                # 先把上一个节点的右指针指向当前节点
                pre.right = root
            # 把当前节点的左指针指向上一个节点
            root.left = pre

            #更新pre指针
            pre = root

            dfs(root.right)
        dfs(root)
        head.left = pre
        pre.right = head
        return head
