#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 57. 插入区间.py
@time: 2020/11/4 11:02
@desc: 
"""
from typing import List
"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]
            # 已经是起点有序的了
        i = 0
        intervalsLen = len(intervals)
        while i < intervalsLen and intervals[i][1] < newInterval[0]:
            i += 1
        # 保存删除之前的位置，最后在这个位置上插入
        if i < intervalsLen:
            # 确定左区间插入位置
            # 此行也可放在46行下面 主要利用其i<intervalslen条件
            newInterval[0] = min(newInterval[0], intervals[i][0])
        tempI = i
        # 左区间小于插入区间的右区间
        while i < intervalsLen and intervals[i][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        else:
            del intervals[tempI:i]
            intervals.insert(tempI, newInterval)
        return intervals


a = Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
print(a)
