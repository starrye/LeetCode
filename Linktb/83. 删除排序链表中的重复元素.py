# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/9 5:14 下午
@file: 83. 删除排序链表中的重复元素.py
@desc: 
"""

from typing import List
"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
返回同样按升序排列的结果链表。

示例 1：


输入：head = [1,1,2]
输出：[1,2]
示例 2：


输入：head = [1,1,2,3,3]
输出：[1,2,3]
 

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
        # dummy = ListNode()
        # dummy.next = head
        # while head and head.next:
        #     if head.val == head.next.val:
        #         head.next = head.next.next
        #     else:
        #         head = head.next
        # return dummy.next

        # new link_table
        dummy = ListNode()
        tail = dummy

        cur = head
        while cur:
            temp = cur.next
            # 如果当前新链表为空或者最后一个元素与当前元素不相等 则添加到新链表的后面
            if tail == dummy or tail.val != cur.val:
                tail.next = cur
                tail = tail.next
            cur = temp
        # 这一步一定要加上 不然可能把旧链表的后续元素加上
        tail.next = None
        return dummy.next