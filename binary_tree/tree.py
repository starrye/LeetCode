#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: tree.py
@time: 2020/5/14 13:45
@desc: 
"""
import json
import sys
from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def stringToTreeNode(input):

    inputValues = [str(s).strip() for s in input]
    root = TreeNode(inputValues[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root



