#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 100.相同的树.py
@time: 2020/4/22 17:44
@desc: 
"""
"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
"""

import json
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
#
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        tree = deque([(p, q)])
        while tree:
            a, b = tree.popleft()
            if not (a or b):
                continue
            if a and b and a.val == b.val:
                tree.append((a.left, b.left))
                tree.append((a.right, b.right))
            else:
                return False
        return True


def stringToTreeNode(input):
    inputValues = [s.strip() for s in input]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root



def main():
    try:
        p = stringToTreeNode(["1","2"])
        q = stringToTreeNode(["1","null","2"])
        Solution().isSameTree(p, q)
    except StopIteration:
        pass


if __name__ == '__main__':
    main()