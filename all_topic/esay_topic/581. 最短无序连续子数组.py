#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 581. 最短无序连续子数组.py
@time: 2020/5/6 14:16
@desc: 
"""
from typing import List

"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = nums[0]
        right = 0
        for i in range(n):
            if (nums[i] >= max_num):
                max_num = nums[i]
            else:
                right = i
        print(right)
        left = n
        min_num = nums[-1]
        for i in range(n - 1, -1, -1):
            if (nums[i] <= min_num):
                min_num = nums[i]
            else:
                left = i
        return right - left + 1 if (right - left + 1 > 0) else 0



# a = Solution().findUnsortedSubarray([2,3,3,2,4])
b = Solution().findUnsortedSubarray([2,6,4,8,10,9,15])
# print(a)
print(b)