# encoding: utf-8
"""
@Project ：
@File: 508. 出现次数最多的子树元素和.py
@Author: liuwz
@time: 2022/6/19 21:27
@desc: 
"""
from collections import defaultdict

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
"""
给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

 

示例 1：



输入: root = [5,2,-3]
输出: [2,-3,4]
示例 2：



输入: root = [5,2,-5]
输出: [2]
 

提示:

节点数在 [1, 104] 范围内
-105 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/most-frequent-subtree-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        tree_sum = defaultdict(int)
        max_count = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            cur_val = left + right + root.val
            tree_sum[cur_val] += 1
            nonlocal max_count
            max_count = max(max_count, tree_sum[cur_val])
            return cur_val
        dfs(root)
        ans = []
        for i, v in tree_sum.items():
            if v == max_count:
                ans.append(i)
        return ans