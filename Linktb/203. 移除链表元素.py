# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/9 5:03 下午
@file: 203. 移除链表元素.py
@desc: 
"""

from typing import List
"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
示例 1：

输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
示例 2：

输入：head = [], val = 1
输出：[]
示例 3：

输入：head = [7,7,7,7], val = 7
输出：[]
 

提示：
列表中的节点在范围 [0, 104] 内
1 <= Node.val <= 50
0 <= k <= 50
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 假头
        # dummy = ListNode(None)
        # dummy.next = head
        # pre = dummy
        # while head:
        #     if head.val == val:
        #         pre.next = head.next
        #     else:
        #         pre = head
        #     head = head.next
        # return dummy.next

        # 新链表
        dummy = ListNode(None)
        cur = dummy

        while head:
            if head.val != val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return dummy.next
