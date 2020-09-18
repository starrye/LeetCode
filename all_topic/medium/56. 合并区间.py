#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 56. 合并区间.py
@time: 2020/9/14 11:24
@desc: 
"""
from typing import List
"""
给出一个区间的集合，请合并所有重叠的区间。
示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。

 

提示：

intervals[i][0] <= intervals[i][1]
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merge = []
        for interval in intervals:
            if not merge or interval[0] > merge[-1][-1]:
                merge.append(interval)
            else:
                merge[-1][-1] = max(merge[-1][-1], interval[1])
        return merge


