#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 234. 回文链表.py
@time: 2020/8/18 10:39
@desc: 
"""
from typing import List
"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1.寻找中间节点
        # 2.反转后半部分
        # 3.分别对比两个链表
        if not head or not head.next:
            return True
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        cur = slow.next
        slow.next = None
        while cur:
            tmp = cur.next
            cur.next = slow
            slow = cur
            cur = tmp
        while slow and head:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True

