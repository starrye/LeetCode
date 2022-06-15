# encoding: utf-8
"""
@Project ：
@File: 436. 寻找右区间.py
@Author: liuwz
@time: 2022/5/20 10:12
@desc: 
"""
from typing import List

""":cvar
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。

区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。

返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

 
示例 1：

输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。
示例 2：

输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。
示例 3：

输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
 

提示：

1 <= intervals.length <= 2 * 104
intervals[i].length == 2
-106 <= starti <= endi <= 106
每个间隔的起点都 不相同
"""


# 1/先按照left排序
# 2/遍历intervals 然后针对right 在intervals的left中进行二分查找
# 3/获取第一个大于等于当前right 即为所求


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals_dict = {v[0]: i for i, v in enumerate(intervals)}

        intervals_list = sorted(intervals_dict.items(), key=lambda x:x[0])
        ans = [0] * len(intervals)
        for start_i, index in intervals_list:
            res = self.bs(intervals_list, index, intervals[index][1])
            ans[index] = res
        return ans

    def bs(self, nums, l, target):
        left = 0
        right = len(nums) - 1
        if target > nums[-1][0]:
            return -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid][0] > target:
                right = mid
            elif nums[mid][0] < target:
                left = mid + 1
            else:
                return nums[mid][1]
        return nums[left][1]


a = Solution().findRightInterval([[3,4],[2,3],[1,2]])
print(a)