#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 142. 环形链表 II.py
@time: 2020/12/16 15:39
@desc: 
"""
from typing import List
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？
 

示例 1：



输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 

提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        设head到环入口的距离为a 环长为b，快指针在圈内走了k1圈 满指针在圈内走了k2圈
        1/快指针走过了 f = a + k1b
        2/慢指针走过了 s = a + k2b
        3/ f - s = (k1 - k2)b
        4/ f = s + (k1 - k2)b *
        5/ f = 2s *
        6/ 结合两个*可得 s = (k1-k2)b
        7/ 设n为快指针与满指针的走的圈数的差值 k1 - k2
        8/ s = nb f = 2nb
        :param head:
        :return:
        """
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