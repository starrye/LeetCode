#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 88. 合并两个有序数组.py
@time: 2020/8/21 11:02
@desc: 
"""
import bisect
from typing import List
"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 折半插入
        # def insert_nums1(k):
        #     left = 0
        #     right = len(nums1) - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if nums1[mid] > k:
        #             right = mid - 1
        #         elif nums1[mid] < k:
        #             left = mid + 1
        #         else:
        #             nums1.insert(mid, k)
        #             return
        #     nums1.insert(left, k)
        # nums1[:] = nums1[:m]
        # for i in range(n):
        #     insert_nums1(nums2[i])
        #     print(nums1)
        # nums1[:] = nums1[:m + n]
        # return nums1
        nums1[:] = nums1[:m]
        for i in range(n):
            index = bisect.bisect(nums1, nums2[i])
            nums1.insert(index, nums2[i])
        return nums1

a = Solution().merge([1,2,3,0,0,0], 3 , [2,5,6], 3)
print(a)