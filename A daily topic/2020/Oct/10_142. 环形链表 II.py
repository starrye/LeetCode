#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 142. 环形链表 II.py
@time: 2020/10/10 15:56
@desc: 
"""
from typing import List
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。

 

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1. 快指针走的是慢指针的2倍
        # 2. 走a + nb步一定在环入口 a为头到环入口 b为环长
        # 3. 第一次相遇时慢指针走了 nb步 结合2 慢指针只需要走a步即可到环入口
        fast = slow = head
        while True:
            if not fast or not fast.next:
                return
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                 break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
