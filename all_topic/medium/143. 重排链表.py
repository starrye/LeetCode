#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 143. 重排链表.py
@time: 2020/10/20 10:02
@desc: 
"""
import json
from typing import List
"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 原链表操作
        # if not head:
        #     return
        # slow, fast = head, head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # # 翻转
        # pre, cur = None, slow.next
        # # 前后断开
        # slow.next = None
        # while cur:
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        #
        # # 拼接
        # p, q = head, pre
        # while q:
        #     temp = p.next
        #     p.next = q
        #     p, q = q, temp

        # 新链表
        mid = self.findMidNode(head)
        back = self.reverse(mid.next)
        mid.next = None
        front = head

        dummy = ListNode()
        tail = dummy

        is_front = True
        while front or back:
            if is_front and front:
                tail.next = front
                tail = tail.next
                front = front.next
            else:
                tail.next = back
                tail = tail.next
                back = back.next
            is_front = not is_front

    def reverse(self, head):
        dummy = ListNode()
        dummy.next = None
        while head:
            temp = head.next
            head.next = dummy.next
            dummy.next = head
            head = temp
        return dummy.next

    def findMidNode(self, head):
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        fast = slow = head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        if fast:
            return slow
        else:
            return pre


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    try:
        # for line in ["1","2","3","4"]:
        head = stringToListNode([1,2,3,4, 5]);

        ret = Solution().reorderList(head)

        out = listNodeToString(head)
        if ret is not None:
            print("Do not return anything, modify head in-place instead.")
        else:
            print(out)
    except StopIteration:
        print('-------')


if __name__ == '__main__':
    main()
