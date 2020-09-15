#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 19. 删除链表的倒数第N个节点.py
@time: 2020/8/17 15:52
@desc: 
"""
from typing import List
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # q = p = ans = ListNode(0)
        # p.next = head
        # while n + 1:
        #     p = p.next
        #     n -= 1
        # while p:
        #     p = p.next
        #     q = q.next
        # q.next = q.next.next
        # return ans.next

        p = q = head
        while p:
            if n < 0:
                q = q.next
            n -= 1
            p = p.next
        if n == 0:
            return head.next
        q.next = q.next.next
        return head
