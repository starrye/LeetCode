# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/20 3:21 下午
@file: 24. 两两交换链表中的节点.py
@desc: 
"""

from typing import List
"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：

输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]
 

提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
 
进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 原链表操作
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return second

        # 新链表
        if not head or not head.next:
            return head
        dummy = ListNode()
        tail = dummy

        first = head
        second = head.next
        while first and second:
            # 保存后续结点
            temp = second.next

            # 反转当前两个结点
            tail.next = second
            second.next = first
            tail = first

            # 往后走两个结点
            first = temp
            second = temp.next if temp else None

        # 奇数个结点时需要处理
        if first:
            tail.next = first
            tail = tail.next
        tail.next = None
        return dummy.next


