#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 55.跳跃游戏_200417.py
@time: 2020/4/17 09:09
@desc: 
"""
"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。。
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if 0 not in nums or len(nums)<2: return True
        # 获取最远距离
        max_distance = nums[0]
        for i in range(1, len(nums)-1):
            if i <= max_distance:
                # 更新坐标
                max_distance = max(max_distance, i + nums[i])
        return max_distance >= len(nums) - 1

        # cur_index = len(nums)-1
        # i = len(nums)-2
        # while i >= 0:
        #     if i + nums[i] >= cur_index:
        #         cur_index = i
        #     i -= 1
        # return cur_index == 0


a = Solution().canJump([3,2,1,0,4])
print(a)