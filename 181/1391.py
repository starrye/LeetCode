#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1391.py
@time: 2020/4/30 10:24
@desc: 
"""

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # x 上下 y 左右
        # 1:y-1 y + 1
        # 2:x-1 x + 1
        # 3:y-1 x + 1
        # 4:y+1 x + 1
        # 5:y-1 x - 1
        # 6:y+1 x - 1
        dict_ = {1:[[0, -1],[0,1]], 2: [[-1, 0],[1,0]], 3:[[0, -1],[1,0]], 4:[[0, 1],[1,0]], 5:[[0, -1],[-1,0]]
                ,6:[[0, 1],[-1,0]]}
        from collections import deque
        current_arrive = deque()
        current_arrive.append((len(grid)-1, len(grid[-1])-1))
        marked = set()
        marked.add((len(grid)-1, len(grid[-1])-1))
        flag = False
        while current_arrive:
            x, y = current_arrive.popleft()
            if (x, y) == (0, 0):
                return True
            marked.add((x, y))
            last_loc = (x, y)
            current_loc = grid[x][y]
            x_y_offsets = dict_[current_loc]
            for x_offset, y_offset in x_y_offsets:
                if (x,y) == (len(grid)-1,len(grid[-1])-1):
                    flag = True
                else:
                    if (x + x_offset, y+y_offset) == last_loc:
                        flag = True
                if 0 <= x + x_offset < len(grid) and 0 <= y + y_offset < len(grid[x+x_offset]) and (
                x + x_offset, y + y_offset) not in marked:
                    current_arrive.append((x + x_offset, y + y_offset))
            if not flag:
                return False
        return False


# a = Solution().hasValidPath([[2,4,3],[6,5,2]])
# b = Solution().hasValidPath([[1,2,1],[1,2,1]])
# c = Solution().hasValidPath([[1,1,2]])
# d = Solution().hasValidPath([[1,1,1,1,1,1,3]])
# e = Solution().hasValidPath([[2],[2],[2],[2],[2],[2],[6]])
f = Solution().hasValidPath([[2,3,6,5,6,1,6,6],[5,6,3,5,1,5,4,2],[5,3,6,1,4,1,6,3],[2,2,4,2,5,6,2,3],[2,2,2,4,6,2,4,5],[1,6,5,6,4,2,4,6],[2,2,6,5,1,3,6,6],[6,5,2,3,2,3,2,6],[2,2,3,3,3,3,6,1],[5,3,3,2,2,2,1,1]])
# print(a==True)
# print(b==False)
# print(c==False)
# print(d==True)
# print(e==True)
print(f)