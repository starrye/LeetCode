#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 384. 打乱数组.py
@time: 2020/8/31 13:52
@desc: 
"""
import random
from typing import List
"""
打乱一个没有重复元素的数组。

 

示例:

// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
"""


class Solution:

    def __init__(self, nums: List[int]):
        self.result = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.result

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.result.copy()
        for i in range(len(nums)):
            j = random.randint(i, len(nums) - 1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()