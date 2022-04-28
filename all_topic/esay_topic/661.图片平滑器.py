# encoding: utf-8
"""
@Project ： 
@File: 661.图片平滑器.py
@Author: liuwz
@time: 2022/3/24 10:39 上午
@desc: 
"""
"""
图像平滑器 是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。

每个单元格的  平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。

如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。
"""

from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        result = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                count, cur_sum = 0, 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < rows and 0 <= col + j < cols:
                            cur_sum += img[row+i][col+j]
                            count += 1
                result[row][col] = cur_sum // count
        return result


a= Solution().imageSmoother([[100,200,100],[200,50,200],[100,200,100]])
print(a)



