#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题30. 包含min函数的栈.py
@time: 2020/5/14 14:38
@desc: 
"""
from typing import List
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]


    def min(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]