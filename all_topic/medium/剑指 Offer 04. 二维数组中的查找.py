# encoding: utf-8
"""
@Project ：
@File: 剑指 Offer 04. 二维数组中的查找.py
@Author: liuwz
@time: 2022/1/2 5:09 下午
@desc: 
"""
from typing import List

"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

限制：
0 <= n <= 1000
0 <= m <= 1000
"""


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix[0]) == 0:return False
        rows = len(matrix)
        cols = len(matrix[0])
        # 右上角开始
        begin = [0, cols - 1]
        while begin[0] < rows and begin[1] >= 0:
            cur_num = matrix[begin[0]][begin[1]]
            if cur_num > target:
                # 行 二分 找到小于target的第一个值
                begin[1] = self.bs(matrix, rows - 1, target, begin, 0)
                # begin[1] -= 1
            elif cur_num < target:
                # 列 二分 找到第一个大于target的值
                # 如果已经到了最后一行 说明已经找不到目标值了
                if begin[0] == rows:
                    return False
                begin[0] = self.bs(matrix, rows - 1, target, begin, 1)
                # begin[0] += 1
            else:
                return True
        return False

    def bs(self, matrix, rows, target, cur_loc, dirc):
        # dirc 0 表示行二分 1 表示列二分
        if dirc:
            left, right = cur_loc[0], rows
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[mid][cur_loc[1]] < target:
                    left = mid + 1
                elif matrix[mid][cur_loc[1]] > target:
                    right = mid - 1
                else:
                    return mid
            return left
        else:
            left, right = 0, cur_loc[1]
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[cur_loc[0]][mid] < target:
                    left = mid + 1
                elif matrix[cur_loc[0]][mid] > target:
                    right = mid - 1
                else:
                    return mid
            return left - 1


# a = Solution().findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 0)
a = Solution().findNumberIn2DArray([[1, 3, 5]], 3)
print(a)
