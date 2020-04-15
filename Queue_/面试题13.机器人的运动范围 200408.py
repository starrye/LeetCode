#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题13.机器人的运动范围 200408.py
@time: 2020/4/8 10:10
@desc: 
"""
import collections

"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
示例 1：
输入：m = 2, n = 3, k = 1
输出：3
示例 1：
输入：m = 3, n = 1, k = 0
输出：1
提示：
1 <= n,m <= 100
0 <= k <= 20
"""



class Solution(object):
    # 坐标数列求和
    def sum_rc(self, row, col):
        sum = 0
        while row > 0:
            sum += row % 10
            row //= 10
        while col > 0:
            sum += col % 10
            col //= 10
        return sum

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # BFS
        # 访问后的点加到集合（标记）中
        marked = set()
        # 定义队列
        queue = collections.deque()
        # 队列添加坐标（0,0）开始
        queue.append((0, 0))
        # 当队列不为空
        while queue:
            # 从队列获取坐标
            x, y = queue.popleft()
            # 坐标不在标记的集合中and当前坐标数列和小于k
            if (x, y) not in marked and self.sum_rc(x, y) <= k:
                # 坐标加入集合中
                marked.add((x, y))
                # 仅考虑向右和向下的组合
                for dx, dy in [(1,0), (0,1)]:
                    # 判断是否超过m与n值
                    if x+dx < m and y+dy < n:
                        # 队列加入新的坐标值
                        queue.append((x+dx, y+dy))
        # 返回集合长度
        return len(marked)
        """
        # DFS_BFS
        def dfs(i, j):
            nonlocal res
            # 如果坐标等于m与n 或者 坐标数列和已经大于k 或者 坐标已经在标记的集合中则返回
            if i == m or j == n or self.sum_rc(i, j) > k or (i, j) in marked:
                return
            # 集合添加坐标
            marked.add((i, j))
            res += 1
            # 对横坐标与纵坐标分别+1 递归调用该函数
            dfs(i+1, j)
            dfs(i, j+1)
        # 初始化集合
        marked = set()
        res = 0
        # 从（0, 0）开始调用递归函数
        dfs(0, 0)
        # 返回集合长度
        return res
        """


a = Solution().movingCount(2,3,1)
print(a)