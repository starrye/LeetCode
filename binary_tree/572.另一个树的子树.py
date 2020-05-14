#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 572.另一个树的子树.py
@time: 2020/5/7 08:47
@desc: 
"""
import json
from typing import List
from binary_tree.tree import stringToTreeNode
#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
示例 1:
给定的树 s:

     3
     
    / \
   4   5
  / \
 1   2
给定的树 t：

   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    #     if not s and not t:
    #         return True
    #     if not s or not t:
    #         return False
    #     return self.issametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    # def issametree(self,s,t):
    #     if not s and not t:
    #         return True
    #     if not s or not t:
    #         return False
    #     return s.val == t.val and self.issametree(s.left, t.left) and self.issametree(s.right, t.right)

    # 先序遍历+判断列表相等
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.t = self.preScan([],t)
        self.s = self.preScan([],s)
        if len(self.t) == len(self.s):
            return self.s == self.t
        print(self.t)
        print(self.s)
        if "-".join(self.t) in "-".join(self.s):
            return True
        return False

    def preScan(self, retList, node):  # 先序遍历：先跟、再左、后右
        if node != None:
            retList.append(node.val)
            self.preScan(retList, node.left)
            self.preScan(retList, node.right)
        else:
            retList.append("null")
        return retList


s = stringToTreeNode([3,4,5,1,2])
t = stringToTreeNode([4,1,2])
a = Solution().isSubtree(s, t)
print(a)


