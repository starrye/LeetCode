# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/6 11:00 上午
@file: 373. 查找和最小的K对数字.py
@desc: 
"""
import heapq
from typing import List

"""
给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。
定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。
找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。
示例 1:

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
示例 2:

输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
示例 3:

输入: nums1 = [1,2], nums2 = [3], k = 3 
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # heap = [[i, j] for i in nums1 for j in nums2]
        # heapq.heapify(heap)
        # return heapq.nsmallest(k, heap, key=lambda x: x[0]+x[1])

        # return heapq.nsmallest(k, [[i, j] for i in nums1 for j in nums2], key=lambda x: x[0]+x[1])

        heap = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        ans = []
        while heap and k > 0:
            s, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            k -= 1

            #  从左上角第一个开始, 斜向扩张
            """
            x 0 0 0     x x 0 0     x x x 0     x x x x
            0 0 0 0 --> x 0 0 0 --> x x 0 0 --> x x x 0 ...
            0 0 0 0     0 0 0 0     x 0 0 0     x x 0 0
            """
            push(i, j + 1)
            if j == 0:
                push(i + 1, j)

        return ans


a = Solution().kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3)
print(a)
