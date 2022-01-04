# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 53 - I. 在排序数组中查找数字 I.py
@Author: liuwz
@time: 2021/12/31 11:02 上午
@desc: 
"""
from typing import List

"""
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = 0
        index = self.binary_search(nums, target)
        if index is not None:
            result += 1
            right, left = index + 1, index - 1
            while right <= len(nums) - 1:
                if nums[right] == target:
                    result += 1
                right += 1
            while left >= 0:
                if nums[left] == target:
                    result += 1
                left -= 1
            return result
        return 0

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return None

a = Solution().search([5,7,7,8,8,8,10], 8)
print(a)

