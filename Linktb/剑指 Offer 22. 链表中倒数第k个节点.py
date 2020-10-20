#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 剑指 Offer 22. 链表中倒数第k个节点.py
@time: 2020/8/17 15:45
@desc: 
"""
from typing import List
"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。
示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 根据题目要求 输出倒数第k个节点
        # 这里假设链表长度为n 那么应该将指针移动到 n - k + 1的位置

        # 1.双指针都从开头开始
        # 2.先将第一个指针移动到k+1的位置(从1开始计算)
        # 3.然后将两个指针同步往后移动 直到第一个指针移动到最后
        # 4.此时第一个指针移动的距离为 n - k +1 即为所求
        if not head:
            return head
        p = head
        q = head
        while k:
            p = p.next
            k -= 1
        while p:
            p = p.next
            q = q.next
        return q
