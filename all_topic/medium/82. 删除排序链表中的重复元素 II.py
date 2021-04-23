# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/12 10:57 上午
@file: 82. 删除排序链表中的重复元素 II.py
@desc: 
"""

from typing import List
"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。
 
示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：

输入：head = [1,1,1,2,3]
输出：[2,3]
 

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while head:
            # 找到重复元素的最后一个元素
            while head.next and head.val == head.next.val:
                head = head.next

            # 如果没有重复元素 pre往下走
            if pre.next == head:
                pre = pre.next

            # 如果有重复元素 pre.next 指向head.next 因为head此时为重复元素的最后一个元素
            else:
                pre.next = head.next

            head = head.next
        return dummy.next




