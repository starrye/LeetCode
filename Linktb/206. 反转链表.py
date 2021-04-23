# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/9 3:29 下午
@file: 206. 反转链表.py
@desc: 
"""

from typing import List
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        dummy = ListNode(None)
        while head:
            temp = head.next
            head.next = dummy.next
            dummy.next = head
            head = temp
        return dummy.next