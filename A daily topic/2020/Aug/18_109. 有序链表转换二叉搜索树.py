#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 109. 有序链表转换二叉搜索树.py
@time: 2020/8/18 10:17
@desc: 
"""
from typing import List
"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def find_mid(head, tail):
            slow = fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return slow

        def help(head, tail):
            if head == tail:
                return
            node = find_mid(head, tail)
            root = TreeNode(node.val)
            root.left = help(head, node)
            root.right = help(node.next, tail)
            return root

        return help(head, None)


















