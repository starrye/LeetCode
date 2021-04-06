# encoding: utf-8
"""
@author: liuwz
@time: 2021/3/31 5:58 下午
@file: 637. 二叉树的层平均值.py
@desc: 
"""
"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

 

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
 

提示：

节点值的范围在32位有符号整数范围内。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # 返回结果
        res = []

        from collections import deque
        # 定义队列
        queue = deque()
        # 将根节点入队
        queue.append(root)
        # 队列不为空，表达式二叉树还有节点，循环遍历
        while queue:
            # 先标记每层的节点数
            size = len(queue)
            # 定义变量，记录每次节点值
            total = 0
            # 这里开始遍历当前层的节点
            for _ in range(size):
                # 出队
                node = queue.popleft()
                # 先将当前节点的值存储
                total += node.val
                # 节点的左右节点非空时，入队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 添加每层的节点值均值
            res.append(total/size)
        return res