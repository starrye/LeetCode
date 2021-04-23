#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 21. 合并两个有序链表.py
@time: 2020/8/17 17:34
@desc: 
"""
from typing import List
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        # 新链表-双指针
        dummy = ListNode()
        tail = dummy

        p = l1
        q = l2
        while p and q:
            if p.val < q.val:
                tail.next = p
                p = p.next
            else:
                tail.next = q
                q = q.next
            tail = tail.next

        if p:
            tail.next = p
        if q:
            tail.next = q
        # 注意：这里一定要记得把tail.next设置为空。
        # 虽然这个题可能并不需要，但是应该养成收尾的好习惯
        tail.next = None
        return dummy.next


