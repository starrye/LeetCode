# encoding: utf-8
"""
@Project ： 
@File: 417. 太平洋大西洋水流问题.py
@Author: liuwz
@time: 2022/4/27 6:50 下午
@desc: 
"""
from collections import deque
from typing import List

""":cvar
有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。

这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。

岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。

返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动 既可流向太平洋也可流向大西洋 。

 

示例 1：
输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
示例 2：

输入: heights = [[2,1],[1,2]]
输出: [[0,0],[0,1],[1,0],[1,1]]
 

提示：

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

""":cvar
思路： 从两个洋的边界开始bfs 收集不严格大于自己的节点 然后求两个洋可达的节点交集
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        tp_visited = set()
        dx_visited = set()

        def bfs(ocean, row, col):
            q_tp = deque()
            q_tp.append((row, col))
            if ocean == 'tp':
                visited = tp_visited
            else:
                visited = dx_visited
            visited.add((row, col))
            while q_tp:
                x, y = q_tp.popleft()
                for n_x, n_y in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if 0 <= n_x < rows and 0 <= n_y < cols and heights[x][y] <= heights[n_x][n_y] and (
                    n_x, n_y) not in visited:
                        visited.add((n_x, n_y))
                        q_tp.append((n_x, n_y))
            return visited

        for row in range(rows):
            bfs("tp", row, 0)
            bfs("dx", row, cols - 1)
        for col in range(cols):
            bfs("tp", 0, col)
            bfs("dx", rows - 1, col)
        return list(tp_visited & dx_visited)

a = Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
print(a)





