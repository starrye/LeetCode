#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 剑指 Offer 06. 从尾到头打印链表.py
@time: 2020/12/3 11:08
@desc: 
"""
from typing import List
"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        count = head
        length = 0
        while count:
            length += 1
            count = count.next
        result = [0] * length
        length -= 1
        while head:
            result[length] = head.val
            length -= 1
            head = head.next
        return result
