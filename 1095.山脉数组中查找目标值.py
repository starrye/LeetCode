#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1095.山脉数组中查找目标值.py
@time: 2020/4/29 10:06
@desc: 
"""
"""
给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。
如果不存在这样的下标 index，就请返回 -1。
何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：
首先，A.length >= 3
其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：

MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
MountainArray.length() - 会返回该数组的长度
 
注意：
对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。
为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。
 
示例 1：

输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
示例 2：

输入：array = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。
 

提示：

3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#        return
#    def length(self) -> int:

class Solution:
    # 查找峰值索引
    # 峰值两端分别二分查找
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binary_search(start, end, left=True):
            while start <= end:
                mid = (start + end) // 2
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    if left:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if left:
                        start = mid + 1
                    else:
                        end = mid - 1
            return -1
        n = mountain_arr.length()
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if mid > 0 and val < mountain_arr.get(mid - 1):
                right = mid - 1
            elif mid < n - 1 and val < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                break
        index = binary_search(0, mid)
        if index != -1:
            return index
        return binary_search(mid + 1, n - 1, False)