#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 34. 在排序数组中查找元素的第一个和最后一个位置.py
@time: 2020/12/1 09:34
@desc: 
"""
from typing import List
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            return [-1, -1]
        print(mid)
        left, right = mid, mid
        while left > 0:
            if nums[left - 1] == target:
                left -= 1
                continue
            break

        while right < end:
            if nums[right + 1] == target:
                right += 1
                continue
            break
        return [left, right]


# a = Solution().searchRange([5,7,7,8,8,10], 8)
b = Solution().searchRange([1,2,3,3,3,3,4,5,9], 3)

# print(a)
print(b)