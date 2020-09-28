#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 117. 填充每个节点的下一个右侧节点指针 II.py
@time: 2020/9/28 10:08
@desc: 
"""
from collections import deque
from typing import List
"""
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

进阶：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 

示例：
输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
 

提示：

树中的节点数小于 6000
-100 <= node.val <= 100
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while queue:
            next_layer = []
            temp_node = None
            while queue:
                node = queue.popleft()
                if temp_node:
                    temp_node.next = node
                temp_node = node
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            node.next = None
            queue = deque(next_layer)
        return root