#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 337. 打家劫舍 III.py
@time: 2020/8/5 09:56
@desc: 
"""
from typing import List
"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
示例 1:
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # from collections import deque
        # if not root:
        #     return 0
        # last_max = 0
        # curr_max = 0
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     next_layer = []
        #     current_val = 0
        #     while queue:
        #         current_node = queue.popleft()
        #         current_val += current_node.val
        #         if current_node.left is not None:
        #             next_layer.append(current_node.left)
        #         if current_node.right is not None:
        #             next_layer.append(current_node.right)
        #     curr_max, last_max = max(last_max + current_val), curr_max
        # return curr_max

        # 那么一个节点如果偷取它，它的偷取收益为
        # node.val + not_steal_left + not_steal_right，即它的左右子节点取不偷取的收益
        # 如果该节点不偷取, 它的左右子节点可以随意选择偷或不偷，那么最大收益为max(steal_left, not_steal_left) + max(steal_right, not_steal_right)
        if not root:
            return 0
        def help(root):
            if not root:
                return 0, 0
            left_not_do, left_do = help(root.left)
            right_not_do, right_do = help(root.right)

            return max(left_not_do, left_do) + max(right_not_do, right_do), left_not_do + right_not_do + root.val
        return max(help(root))




