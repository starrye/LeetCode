#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 48. 旋转图像.py
@time: 2020/8/7 10:23
@desc: 
"""
from typing import List
"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
示例 1:
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1.按照列遍历，增加到对应行
        # 2.遍历数组，删除每一行的前n个数
        # length = len(matrix)
        # if length == 1:
        #     return matrix
        # row = 0
        # while row < length:
        #     col = length - 1
        #     while col >= 0:
        #         matrix[row].append(matrix[col][row])
        #         col -= 1
        #     row += 1
        # print(matrix)
        # i = 0
        # while i < length:
        #     matrix[i] = matrix[i][length:]
        #     i += 1
        # print(matrix)

        # 两次反转
        # 行变列(对角线反转)
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        # 每行反转(轴对称)
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]



a = Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])




