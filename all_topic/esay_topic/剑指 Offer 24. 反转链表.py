#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 剑指 Offer 24. 反转链表.py
@time: 2020/8/17 17:07
@desc: 
"""
from typing import List
"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        current = head.next
        head.next = None
        while current:
            q = current.next
            current.next = head
            head = current
            current = q
        return head

