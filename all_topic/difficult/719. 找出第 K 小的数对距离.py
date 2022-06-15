# encoding: utf-8
"""
@Project ： 
@File: 719. 找出第 K 小的数对距离.py
@Author: liuwz
@time: 2022/6/15 10:37 AM
@desc: 
"""
import heapq

import pandas as pd
import numpy as np
from typing import List

"""
数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。

给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length 。返回 所有数对距离中 第 k 小的数对距离。

 

示例 1：

输入：nums = [1,3,1], k = 1
输出：0
解释：数对和对应的距离如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
距离第 1 小的数对是 (1,1) ，距离为 0 。
示例 2：

输入：nums = [1,1,1], k = 2
输出：0
示例 3：

输入：nums = [1,6,1], k = 3
输出：5
 

提示：

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2

"""
# 1/ 观察数据范围 10**6  O(n^2)是不符合要求的 考虑O(nlogn) 二分
# 2/ 数组排序
# 3/ 注意这里的二分的l和r 代表的是差值的小值和差值的大值 而非数组的元素
# 4/ 双指针对数组判断距离对差值 小于当前中值的 数量 (注意双指针的复杂度为O（n）因为，i和j都在向前走)
# 5/ 重复 3/4 直到找到最左侧符合要求的第k小的数对距离-这里为什么是最左侧，因为我们是对差值做的二分，不能保证元素一定存在，所以往左侧继续搜索，找到一个保证差值一定存在且符合标准的

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        # while l <= r:
        while l < r:
            mid = l + (r - l) // 2
            i, count = 0, 0
            for j in range(len(nums)):
                while nums[j] - nums[i] > mid:
                    i += 1
                count += j - i
            if count >= k:
                # r = mid - 1
                r = mid
            else:
                l = mid + 1
        return l


a = Solution().smallestDistancePair([1, 3, 1], 1)
print(a)
