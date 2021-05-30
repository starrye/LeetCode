#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 130. 被围绕的区域.py
@time: 2020/8/11 11:05
@desc: 
"""
from collections import deque
from typing import List
"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""

class UF:
    def __init__(self, n):
        # 集合关系
        self.parent = {}
        # 每个集合内数量
        self.Cnt = {}
        for i in range(n):
            self.parent[i] = i
            self.Cnt[i] = 1
        # 集合数量
        self.count = n

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

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # uf
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])
        dir = [[0, 1], [1, 0]]
        # 虚拟点 用于作为所有边上的点的父结点
        vir_node = rows * cols
        # 由于多了一个父结点 所以初始化时增加一个点
        uf = UF(rows * cols + 1)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    # 所有边缘的点直接与虚拟点相连
                    if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                        uf.union((row * cols + col), vir_node)
                    # 遍历"O"的右侧与下侧
                    for row_x, col_y in dir:
                        new_row = row + row_x
                        new_col = col + col_y
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            if board[new_row][new_col] == "O":
                                uf.union((row * cols + col), (new_row * cols + new_col))
        print(uf.parent)
        # 寻找不与虚拟点(与边缘点有关联)的点 改为X
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and uf.find(row * cols + col) != uf.find(vir_node):
                    board[row][col] = "X"

        return board


        # bfs
        # rows = len(board)
        # if rows == 0: return board
        # cols = len(board[0])
        # if cols == 0: return board
        # border_zero = set()
        # border_zero_queue = deque()
        # inside_zero = set()
        #
        # # 边界 "O" 加入 border_zero_queue
        # # 内部 "O" 加入 inside_zero
        # for row in range(rows):
        #     for col in range(cols):
        #         if board[row][col] == "O":
        #             if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
        #                 border_zero_queue.append([row, col])
        #             else:
        #                 inside_zero.add((row, col))
        #
        # # 边界 "O" 相连的 "O" 同样加入border_zero_queue，
        # # 这一步主要是把所有可修改的"O"位置找出来(把边界 "O" 相连的 "O"从inside_zero中除去)
        # while border_zero_queue:
        #     x, y = border_zero_queue.popleft()
        #     border_zero.add((x, y))
        #     for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        #         if 0 <= x + dx < rows and 0 <= y + dy < cols and board[x+dx][y+dy] == "O" and (x+dx, y+dy) not in border_zero:
        #             border_zero_queue.append([x+dx, y+dy])
        #             if (x+dx, y+dy) in inside_zero:
        #                 inside_zero.remove((x+dx, y+dy))
        #
        # # 此时inside_zero中全部都是可修改的
        # while inside_zero:
        #     x, y = inside_zero.pop()
        #     board[x][y] = "X"



# a = Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# b = Solution().solve([["X","X","X"],["X","O","X"],["X","X","X"]])
# c = Solution().solve([["X","O","X"],["X","O","X"],["X","O","X"]])
# d = Solution().solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])
# print(a)
# print(b)
# print(c)
# print(d)

d = Solution().solve([["O","O","O","O","X","X"],
                      ["O","O","O","O","O","O"],
                      ["O","X","O","X","O","O"],
                      ["O","X","O","O","X","O"],
                      ["O","X","O","X","O","O"],
                      ["O","X","O","O","O","O"]])
print(d)