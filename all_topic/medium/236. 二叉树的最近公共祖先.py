#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 236. 二叉树的最近公共祖先.py
@time: 2020/5/10 11:29
@desc: 
"""
from typing import List
"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
"""
from binary_tree.tree import stringToTreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 存储子结点与根的关系 反向查找
        # relation_dic = {root: None}
        # def dfs(node):
        #     """利用递归实现树的先序遍历"""
        #     if node == None:
        #         return
        #     if node.left:
        #         relation_dic[node.left] = node
        #     if node.right:
        #         relation_dic[node.right] = node
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # l1, l2 = p, q
        # while l1 != l2:
        #     l1 = relation_dic[l1, q]
        #     l2 = relation_dic[l2, p]
        # return l1

    # 后序遍历实现
    # 统计结点p q的个数 然后利用返回的个数 得到最低的公共祖先
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.help(root, p, q)
        return self.ans

    def help(self, root, p, q):
        if not root:
            return 0

        # 查看子结点的统计个数
        lcount = self.help(root.left, p, q)
        rcount = self.help(root.right, p, q)

        # 左右子树刚好都找到了p q 那么root就是最低公共祖先
        if lcount == 1 and rcount == 1:
            self.ans = root
        # 左右子树只有一个确定了
        elif lcount + rcount == 1:
            # 并且当前结点正好是另外一个
            # 那么当前结点就是最低公共祖先
            if root == p or root == q:
                self.ans = root
        # 返回以root为根的子树 统计里面的p q结点的个数
        return lcount + rcount + (1 if (root == p or root == q) else 0)


root = stringToTreeNode([3,5,1,6,2,0,8,"null","null",1,6])
a = Solution().lowestCommonAncestor(root, 5, 1)
print(a)