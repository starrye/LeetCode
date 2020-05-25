#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 341. 扁平化嵌套列表迭代器.py
@time: 2020/5/22 15:35
@desc: 
"""
from typing import List
"""
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

 

示例 1:

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
示例 2:

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # 对于nestedList中的内容，我们需要从左往右遍历，
        # 但堆栈pop是从右端开始，所以我们压栈的时候需要将nestedList反转再压栈
        self.stack = nestedList[::-1]

    def next(self) -> int:
        # hasNext 函数中已经保证栈顶是integer，所以直接返回pop结果
        return self.stack.pop(-1).getInteger()

    def hasNext(self) -> bool:
        # 对栈顶进行‘剥皮’，如果栈顶是List，把List反转再依次压栈，
        # 然后再看栈顶，依次循环直到栈顶为Integer。
        # 同时可以处理空的List，类似[[[]],[]]这种test case
        while len(self.stack) > 0 and self.stack[-1].isInteger() is False:
            self.stack += self.stack.pop().getList()[::-1]
        return len(self.stack) > 0