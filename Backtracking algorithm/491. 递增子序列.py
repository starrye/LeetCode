#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 491. 递增子序列.py
@time: 2020/8/25 10:01
@desc: 
"""
from collections import defaultdict
from typing import List
"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # result = []
        #
        # def help(nums, start, temp):
        #     if len(temp) >= 2:
        #         result.append(temp[:])
        #     used = set()
        #     for i in range(start, len(nums)):
        #         # 做选择
        #         if nums[i] in used:  # 避免选择重复的数字
        #             continue
        #         if not temp or nums[i] >= temp[-1]:  # 为空则添加数字 然后递归
        #             temp.append(nums[i])
        #             used.add(nums[i])
        #             help(nums, i+1, temp)
        #             print(temp)
        #             # 撤销选择
        #             temp.pop()
        #
        # help(nums, 0, [])
        # return result

        result = []

        def dfs(nums: List[int], tmp: List[int]) -> None:
            print(result)
            if len(tmp) > 1:
                result.append(tmp)
            used = set()
            for inx, i in enumerate(nums):
                if i in used:
                    continue
                if not tmp or i >= tmp[-1]:
                    used.add(i)
                    dfs(nums[inx + 1:], tmp + [i])

        dfs(nums, [])
        return result

a = Solution().findSubsequences([4,6,7,7])
print(a)

