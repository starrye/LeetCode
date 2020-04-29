#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 33.搜索旋转排序数组.py
@time: 2020/4/27 09:20
@desc: 
"""
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

"""
"""
nums[0]<=nums[max]说明整个数组是有序的，下标0就是最小值
如果num[i]>nums[i+1]，不满足升序，说明mid+1就是最小值，退出查找
如果中间值numd[mid]>=nums[0]说明数组左边是有序的，最小值应该在右边
如果中间值nums[mid]<nums[0]说明数组左边是无序的，最小值应该在数组左边
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return - 1
        def find_min_num():
            i = 0
            j = len(nums) - 1
            mid = (i + j) // 2
            if nums[i] <= nums[j]:
                return i
            while i <= j:
                if nums[mid] > nums[mid+1]:
                    return mid + 1
                if nums[mid] >= nums[0]:
                    i = mid + 1
                else:
                    j = mid - 1
                mid = (i + j) // 2
            return 0

        def binary_search(begin, end):
            while begin <= end:
                mid = (begin + end) // 2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    begin = mid + 1
                else:
                    return mid
            return -1
        mid = find_min_num()
        print(mid)
        if mid == 0:
            return binary_search(0,len(nums) - 1)
        if target >= nums[0]:
            return binary_search(0, mid-1)
        return binary_search(mid, len(nums) - 1)


a = Solution().search([5,1,3], 5)
# print(a)