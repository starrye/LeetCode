#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 199.二叉树的右视图.py
@time: 2020/4/22 09:04
@desc: 
"""
import json
from binary_tree.tree import stringToTreeNode
"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS
        # 层次遍历 从根节点遍历，先加入右子树 再加入左子树 然后获取第一个元素
        if not root:
            return []
        res = []
        from collections import deque
        current_layer = deque()
        current_layer.append(root)
        while current_layer:
            count = 0
            next_layer = []
            # 此次循环为了 获取本层的第一个元素 同时把本层所有元素的子节点(右左顺序)加入队列中
            while current_layer:
                tmp_node = current_layer.popleft()
                if count == 0:
                    res.append(tmp_node.val)
                count += 1
                if tmp_node.right is not None:
                    next_layer.append(tmp_node.right)
                if tmp_node.left is not None:
                    next_layer.append(tmp_node.left)
            current_layer = deque(next_layer)
        return res


root = stringToTreeNode([1,2,3,"null",5,"null",4])
ret = Solution().rightSideView(root)

print(ret)


