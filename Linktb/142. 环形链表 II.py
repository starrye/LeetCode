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
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 有环
            if fast == slow:
                # 寻找入口
                # f为快指针走的长度 s为慢指针走的长度
                # a为链表头到环入口的长度 b 为环的长度 n为走过环的圈数
                # f = 2s f = s+nb ==> s = nb f = 2nb
                # 则只需让s再走过a 此时s = a+nb则一定是入口处
                # 怎么让s走a呢 就是 找个指针从头开始走 他们一定在入口处相遇
                # 因为 从头走过a 与 a+nb都是环入口
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
