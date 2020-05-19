#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题59 - I. 滑动窗口的最大值.py
@time: 2020/5/14 14:41
@desc: 
"""
import math
from typing import List

"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = []
        result = []
        for i in range(0, len(nums)):
            # 保证能取到的最大值在头部
            while deque and nums[i] > nums[deque[-1]]:  # 只存有可能成为最大值的数字的index进deque
                deque.pop()
            deque.append(i)
            while i - deque[0] > k - 1:  # 如果相距超过窗口k长度则弃掉
                deque.pop(0)
            if i >= k - 1:
                result.append(nums[deque[0]])  # 这过程中始终保持deque[0]为最大值的index
        return result


a = Solution().maxSlidingWindow([1,3,-1,4,3,5,3,6,7],3)
print(a)




