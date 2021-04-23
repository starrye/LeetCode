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

        # p = q = head
        # while p:
        #     if n < 0:
        #         q = q.next
        #     n -= 1
        #     p = p.next
        # if n == 0:
        #     return head.next
        # q.next = q.next.next
        # return head

        """
        在原链表前面加上 dummy，变成带假头的链表
        front 指针从 dummy 开始，走 k 步，然后停下来
        back 指针指向链表 dummy 假头
        然后两个指针再一起走
        当 front 指针指向最后一个结点时，back 指针刚好指向倒数第 k 个结点的前驱。
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        while n > 0 and first and first.next:
            first = first.next
            n -= 1

        while first and first.next:
            first = first.next
            second = second.next
        # 如果k小于等于链表的长度
        if n == 0:
            second.next = second.next.next

        return dummy.next
