#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1424.对角线遍历II.py
@time: 2020/4/26 10:30
@desc: 
"""


class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # 同一条线上的点的横纵坐标和相同
        from collections import defaultdict
        tmp = defaultdict(list)
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                tmp[row+col].append(nums[row][col])
        res = []
        for key in tmp.keys():
            res.extend(tmp[key][::-1])
        return res

        # result = []
        # # 已遍历的点 (set 判断 x in set 时间复杂度O(1))
        # marked = set()
        # from collections import deque
        # current_layer = deque()
        # result.append(nums[0][0])
        # current_layer.append((0, 0))
        # while current_layer:
        #     # 下一层需要遍历的点
        #     next_layer = []
        #     # 此次循环为了将本层所有的点收录到next_layer中
        #     while current_layer:
        #         x, y = current_layer.popleft()
        #         # 假如把（0,0）点作为左下角的点 那么 每个点都是往上或者往右走
        #         for x_offset, y_offset in [[x+1, y], [x, y+1]]:
        #             if 0 <= x_offset < len(nums) and 0 <= y_offset < len(nums[x_offset]) and (x_offset, y_offset) not in marked:
        #                 marked.add((x_offset, y_offset))
        #                 result.append(nums[x_offset][y_offset])
        #                 next_layer.append((x_offset, y_offset))
        #     current_layer = deque(next_layer)
        # return result


# a = Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
a = Solution().findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]])
print(a)
