# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/22 10:36 上午
@file: 拆分链表.py
@desc: 
"""

from typing import List
"""
给定一个链表，需要把链表从中间拆分成长度相等的两半（如果链表长度为奇数，那么拆分之后，前半部分长度更长一点）。
输入：[1->2->3->4->5]
输出：[1->2->3, 4->5]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def findMiddleNode(self, head):
        dummy = ListNode()
        dummy.next = head

        pre = dummy
        first = slow = head
        while first and first.next:
            pre = slow
            first = first.next.next
            slow = slow.next

        if first:
            return slow
        else:
            return pre


    def split(self, head):
        """
        分析:
        快慢指针
        1/如果链表长度为奇数个 快指针指向最后一个结点 慢指针指向中间结点 所以直接返回慢指针就行
        2/如果链表长度为偶数个 快指针指向空  慢指针指向后面链表的第一个结点 所以需要返回慢指针的前缀结点

        :param head:
        :return:
        """
        mid_node = self.findMiddleNode(head)
        second_linktb = mid_node.next
        mid_node.next = None
        return [head, second_linktb]