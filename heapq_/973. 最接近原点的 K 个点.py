#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 973. 最接近原点的 K 个点.py
@time: 2020/11/9 09:47
@desc: 
"""
from collections import Counter
from heapq import heappush, heappop, heapify, nsmallest
from typing import List
"""
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

 

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
 

提示：

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # return sorted(points, key= lambda x:(x[1]**2+x[0]**2))[:K]

        # queue = []
        # distance = lambda x: points[x][0] ** 2 + points[x][1] ** 2
        # length = len(points)
        # for i in range(length):
        #     print((distance(i), points[i]))
        #     heappush(queue, (distance(i), points[i]))
        # res = []
        # for i in range(K):
        #     res.append(heappop(queue)[1])
        # return res

        # heap = [[i[0]**2 + i[1]**2, i] for i in points]
        # heapify(heap)
        # return [heappop(heap)[1] for _ in range(K)]

        return [x[1] for x in nsmallest(K, [[i[0]**2 + i[1]**2, i] for i in points])]


a = Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
print(a)

