#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题51.数组中的逆序对_200424.py
@time: 2020/4/24 08:54
@desc: 
"""
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:

输入: [7,5,6,4]
输出: 5
限制：

0 <= 数组长度 <= 50000
"""


class Solution:
    def reversePairs(self, nums) -> int:
        self.cnt = 0
        def merge(nums, start, mid, end):
            i, j, temp = start, mid + 1, []
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.cnt += mid - i + 1
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1

            for i in range(len(temp)):
                nums[start + i] = temp[i]

        def mergeSort(nums, start, end):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid, end)

        mergeSort(nums, 0, len(nums) - 1)
        return self.cnt


a =Solution().reversePairs([7,5,6,4])
print(a)