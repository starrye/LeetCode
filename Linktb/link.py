#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: link.py
@time: 2020/10/20 15:09
@desc: 
"""
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

