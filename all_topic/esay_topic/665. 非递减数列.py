#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 665. 非递减数列.py
@time: 2020/5/9 10:54
@desc: 
"""
from typing import List

"""
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，总满足 array[i] <= array[i + 1]。

示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
 

说明：

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        need_change_num = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if need_change_num:
                    return False
                need_change_num = True
                if i != 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
        return True
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         if i == 0:
        #             nums[i] = nums[i+1]
        #         elif nums[i-1] > nums[i+1]:
        #             nums[i+1] = nums[i]
        #         elif nums[i-1] < nums[i+1]:
        #             nums[i] = nums[i+1]
        #         break
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         return False
        # return True


a = Solution().checkPossibility([4,2,3])
b = Solution().checkPossibility([4,2,1])
c = Solution().checkPossibility([-4,-2,-1])
d = Solution().checkPossibility([3,4,2,3])
e = Solution().checkPossibility([1,5,4,6,7,10,8,9])
f = Solution().checkPossibility([3,2,3,2,4])
g = Solution().checkPossibility([2,3,3,2,4])
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)