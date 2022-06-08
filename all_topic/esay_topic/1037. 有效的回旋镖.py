# encoding: utf-8
"""
@Project ： 
@File: 1037. 有效的回旋镖.py
@Author: liuwz
@time: 2022/6/8 2:08 PM
@desc: 
"""

import pandas as pd
import numpy as np
from typing import List
"""
给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，如果这些点构成一个 回旋镖 则返回 true 。

回旋镖 定义为一组三个点，这些点 各不相同 且 不在一条直线上 。

 

示例 1：

输入：points = [[1,1],[2,3],[3,2]]
输出：true
示例 2：

输入：points = [[1,1],[2,2],[3,3]]
输出：false
 

提示：

points.length == 3
points[i].length == 
"""

# 1/三点共线 可以利用斜率 转化为 两式相乘 这样就不用判断分母为0的情况

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # from fractions import Fraction
        # k1 = Fraction(points[1][1] - points[0][1], points[1][0] - points[0][0]) if points[1][0] - points[0][0] != 0 else 0
        # k2 = Fraction(points[2][1] - points[1][1], points[2][0] - points[1][0]) if points[2][0] - points[1][0] != 0 else 0
        # return k1 != k2

        return (points[1][1] - points[0][1]) * (points[2][0] - points[0][0]) != (points[2][1] - points[0][1]) * (points[1][0] - points[0][0])