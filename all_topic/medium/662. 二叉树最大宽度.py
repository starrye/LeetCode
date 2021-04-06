# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/1 11:07 上午
@file: 662. 二叉树最大宽度.py
@desc: 
"""
from collections import deque
from queue import Queue

"""
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。
每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
示例 1:
输入: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
示例 2:

输入: 

          1
         /  
        3    
       / \       
      5   3     

输出: 2
解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
示例 3:

输入: 

          1
         / \
        3   2 
       /        
      5      

输出: 2
解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
示例 4:

输入: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
输出: 8
解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
注意: 答案在32位有符号整数的表示范围内。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # 利用栈模拟队列
        # if not root:
        #     return 0
        # q = [(root, 0)]
        # ans = 0
        # while q:
        #     ans = max(ans, q[-1][1] - q[0][1] + 1)
        #     qsize = len(q)
        #     for _ in range(qsize):
        #         node = q.pop(0)
        #         if node[0].left:
        #             # 当前结点的左子树位置为 i * 2
        #             q.append((node[0].left, node[1] * 2))
        #
        #         if node[0].right:
        #             # 当前结点的右子树位置为 i * 2 + 1
        #             q.append((node[0].right, node[1] * 2 + 1))
        # return ans

        # 利用队列
        if not root:
            return 0
        import queue
        q = queue.Queue()
        # 队列加入结点和位置信息
        q.put((root, 0))
        ans = 0
        while not q.empty():
            qsize = q.qsize()
            # start 当前层的起始位置 end 当前层的结束位置
            start = -1
            end = 0
            for _ in range(qsize):
                node = q.get()
                # 如果start还未赋值，则将其赋值为第一个元素的位置
                if start == -1:
                    start = node[1]
                # end 不停赋值 直到遍历到最后一个元素
                end = node[1]

                if node[0].left:
                    # 当前结点的左子树位置为 i * 2
                    q.put((node[0].left, node[1] * 2))

                if node[0].right:
                    # 当前结点的右子树位置为 i * 2 + 1
                    q.put((node[0].right, node[1] * 2 + 1))
            ans = max(ans, end - start + 1)
        return ans