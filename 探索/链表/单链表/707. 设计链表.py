#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 707. 设计链表.py
@time: 2020/12/16 14:12
@desc: 
"""
from typing import List
"""
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 

示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3
 

提示：

所有val值都在 [1, 1000] 之内。
操作次数将在  [1, 1000] 之内。
请不要使用内置的 LinkedList 库。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.obj = ListNode(0)

    def findPre(self, index):
        pre = self.obj
        while index > 0 and self.obj.next:
            pre = pre.next
            index -= 1
        return pre

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.obj.val:
            return -1
        return self.findPre(index).next.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.obj.val, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.obj.val:
            return
        node = ListNode(val)
        pre = self.findPre(index)
        print(pre.val)
        node.next = pre.next
        pre.next = node
        self.obj.val += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.obj.val:
            return
        pre = self.findPre(index)
        pre.next = pre.next.next
        self.obj.val -= 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(7)

obj.addAtTail(7)

obj.addAtHead(9)
print('------1')
obj.addAtTail(8)
print('------2')
# for i in range(4):
    # print(obj.get(i))
obj.addAtHead(6)
obj.addAtHead(0)
for i in range(6):
    print(obj.get(i))
print(obj.get(5))
obj.addAtHead(0)
print(obj.get(2))
print(obj.get(5))
obj.addAtTail(4)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)