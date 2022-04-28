# encoding: utf-8
"""
@Project ： 
@File: 三数之和.py
@Author: liuwz
@time: 2022/1/10 5:09 下午
@desc: 
"""
from typing import List

"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]
 

提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []
        nums.sort()
        ans = []
        for i, v in enumerate(nums):
            if v > 0:
                return ans
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = [nums[i], nums[left], nums[right]]
                cur_sum = sum(temp)
                if cur_sum == 0:
                    ans.append(temp)
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                    left += 1
                elif cur_sum > 0:
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif cur_sum < 0:
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
        return ans


a= Solution().threeSum([-1,0,1,2,-1,-4])
print(a)