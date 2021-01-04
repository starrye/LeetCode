#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 350. 两个数组的交集 II.py
@time: 2020/7/13 09:30
@desc: 
"""
from typing import List
"""
给定两个数组，编写一个函数来计算它们的交集。
示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        i = 0
        j = 0
        while i < nums1_length and j < nums2_length:
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return result

    """
            # list1 = []
            # if len(nums1) < len(nums2):
            #     for i in nums1:
            #         if i in nums2:
            #             list1.append(i)
            # else:
            #     for i in nums2:
            #         if i in nums1:
            #             nums1.remove(i)
            #             list1.append(i)
            # return list(set(list1))

            list = set(nums1) & set(nums2)
            l = []
            for i in list:
                l += [i] * min(nums1.count(i),nums2.count(i))
            return l
    """


a = Solution().intersect([1,2,2,1], [2,2])
b = Solution().intersect([4,9, 5], [9, 4, 9, 8,4])
print(a)
print(b)