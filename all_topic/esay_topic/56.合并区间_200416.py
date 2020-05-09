#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 56.合并区间_200416.py
@time: 2020/4/16 09:06
@desc: 
"""
"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merge = []
        for interval in intervals:
            if not merge or interval[0] > merge[-1][1]:
                merge.append(interval)
            else:
                merge[-1][1] = max(merge[-1][1], interval[1])
        return merge
        # if len(intervals) == 1:
        #     return intervals
        # intervals.sort(key=lambda x: x[0])
        # i = 1
        # while i < len(intervals):
        #     # i头 <= i-1尾
        #     if intervals[i][0] <= intervals[i-1][1]:
        #         # i 尾 > i-1 尾
        #         if intervals[i][1] > intervals[i-1][1]:
        #             # i 头 = i-1 头
        #             if intervals[i][0] == intervals[i-1][0]:
        #                 # 删除 i-1
        #                 intervals.pop(i-1)
        #             else:
        #                 # 合并 i-1头与i尾
        #                 intervals[i][0] = intervals[i - 1][0]
        #                 intervals.pop(i - 1)
        #         else:
        #             # 删除 i
        #             intervals.pop(i)
        #     else:
        #         i += 1
        # return intervals


a = Solution().merge([[1,4],[1,5]])
b = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
c = Solution().merge([[1,4],[4,5]])
d = Solution().merge([[1,4],[0,1]])
e = Solution().merge([[1,4],[2,3]])
print(a)
print(b)
print(c)
print(d)
print(e)
