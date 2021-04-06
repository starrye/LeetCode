#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 347. 前 K 个高频元素.py
@time: 2020/9/7 10:55
@desc: 
"""
from typing import List
"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
"""
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [e[0] for e in collections.Counter(nums).most_common(k)]

        count = collections.Counter(nums)
        # print(count)
        # 因为python里面的heapq是小顶堆，所以这里把出现次数变成负数入队，次数最多的即为最小值
        heap = [(-c, n) for n, c in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


a = Solution().topKFrequent([3,0,1,0], 1)
print(a)