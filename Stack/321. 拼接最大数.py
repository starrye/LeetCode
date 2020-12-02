#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 321. 拼接最大数.py
@time: 2020/12/2 10:42
@desc: 
"""
from typing import List
# 建议和402 1081 316 一起看
"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
"""
class Solution:
    def maxNumber(self, nums1, nums2, k):
        # 在nums中选择出k个可组成最大数组的值
        def pick_num(nums, k):
            stack = []
            drop = len(nums) - k

            for i in nums:
                # stack 维护结果数组
                # 如果发现当前数字比stack最后以为大 则去掉stack最后一个元素
                # 比如 stack[7,5,3] 当前元素为4 明显stack[-1] < 4 则删除掉3

                while drop and stack and stack[-1] < i:
                    stack.pop()
                    drop -= 1
                stack.append(i)
            return stack[:k]

        # 两个数组分别选出 k1个值 k-k1个值的元素 然后合并
        def merge(n1, n2):
            result = []
            while n1 or n2:
                bigger = n1 if n1 > n2 else n2
                result.append(bigger[0])
                bigger.pop(0)
            return result

        max_ans = [float("-inf")]
        for i in range(k+1):
            if i <= len(nums1) and k - i <= len(nums2):
                max_ans = max(merge(pick_num(nums1, i), pick_num(nums2, k - i)), max_ans)
        return max_ans


a = Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
print(a)
