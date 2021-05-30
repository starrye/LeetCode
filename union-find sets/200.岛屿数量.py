#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 200.岛屿数量_200420.py
@time: 2020/4/20 08:59
@desc: 
"""
"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
"""


class UF:
    def __init__(self, N):
        # 集合关系
        self.parent = {}
        # 每个集合内数量
        self.Cnt = {}
        # 集合数量
        self.count = 0
        for i in range(N):
            self.parent[i] = i
            self.Cnt[i] = 1
        self.count = N

    # 任意节点找根节点 根节点的父节点是自己
    def find(self, x):
        # 路径压缩 简单来说就是 把糖葫芦造型的数据 改成 一把扇子 每一扇叶都直接和扇柄相连
        if x == self.parent[x]:
            return x
        # 此过程把当前节点指向根节点 等于做了完全压缩
        # 比如 1->3->4->5 在此过程 把1的父节点更新为(把3的父节点更新为(找到4的根节点5)->5)->5
        # 其实就是从最底层更新时采用递归 在递归过程中顺便把父节点也更新为根节点  ！！！因为最终递归的出口是根节点
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 合并两个集合
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        # 如果两个集合本身就在同一个根节点下则返回
        if x_parent == y_parent:
            return
        # x的根节点变成y的根节点的子节点
        self.parent[x_parent] = y_parent
        self.Cnt[y_parent] += self.Cnt[x_parent]
        self.count -= 1

    # 返回任意集合的size
    def size(self, x):
        return self.Cnt[self.find(x)]

    # 返回集合数量
    def Count(self):
        return self.count


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # BFS
        # res = 0
        # from collections import deque
        # queue_ = deque()
        # def bfs(x, y):
        #     grid[x][y] = "0"
        #     while queue_:
        #         x, y = queue_.popleft()
        #         for x_offset, y_offset in [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]:
        #             if 0 <= x_offset < len(grid) and 0 <= y_offset < len(grid[0]) and grid[x_offset][y_offset] == "1":
        #                 queue_.append([x_offset, y_offset])
        #                 grid[x_offset][y_offset] = "0"
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == "1":
        #             queue_.append((row, col))
        #             bfs(row, col)
        #             res += 1
        # return res

        # DFS
        # res = 0
        # def dfs(x, y):
        #     grid[x][y] = "0"
        #     for x_offset, y_offset in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
        #         if 0 <= x_offset < len(grid) and 0 <= y_offset < len(grid[0]) and grid[x_offset][y_offset] == "1":
        #             dfs(x_offset, y_offset)
        #             grid[x_offset][y_offset] = "0"
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == "1":
        #             dfs(row, col)
        #             res += 1
        # return res

        # UF
        zero_set = 0
        rows = len(grid)
        cols = len(grid[0])
        R = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        # 二维列表转化为一维的并查集
        # 初始化有多少个元素就有多少个集合
        # 目的是 把所有相邻的1并入到一个集合中 同时统计所有0的集合 最后 集合数目 - 0的集合数目 = 连通1的集合数目
        uf = UF(rows * cols)

        # 二维转化为一维的位置确认
        def uf_index(r, c):
            return r * cols + c

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    for x, y in R:
                        new_row = row+x
                        new_col = col+y
                        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1":
                            uf.union(uf_index(row, col), uf_index(new_row, new_col))
                else:
                    zero_set += 1
        return uf.count - zero_set


a = Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(a)
