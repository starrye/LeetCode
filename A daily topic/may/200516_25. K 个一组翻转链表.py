#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 25. K 个一组翻转链表.py
@time: 2020/5/16 11:00
@desc: 
"""
from typing import List
"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

 

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prenode = ListNode(-1)
        prenode.next = head
        p = prenode
        p_list = [None for _ in range(k)]
        while True:
            # 构建前驱节点
            prenode_tmp = p
            # 获取交换节点
            for i in range(k):
                if p == None:
                    break
                p = p.next
                p_list[i] = p
            # 当前k个范围内有终点 则直接返回
            if p is None:
                break
            # 反转第一步:prenode指向p_list最后一个元素的地址，p_list第一元素位置指向最后一个元素的下一个元素地址
            prenode_tmp.next = p_list[-1]
            p_list[0].next = p_list[-1].next
            # 反转元素：具体做法 倒序遍历，当前元素的指针指向前一个元素的地址
            for i in range(k-1, 0, -1):
                p_list[i].next = p_list[i-1]
            # 修改前驱节点为P_list第一个元素的地址
            p = p_list[0]
        return head