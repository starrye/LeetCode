# encoding: utf-8
"""
@author: liuwz
@time: 2021/3/29 2:33 下午
@file: 剑指 Offer 59 - I. 滑动窗口的最大值.py
@desc: 
"""
from collections import deque

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
    def __init__(self):
        self.Q = deque()

    def push(self, val):
        while self.Q and val > self.Q[-1]:
            self.Q.pop()
        self.Q.append(val)

    def pop(self, val):
        if self.Q and self.Q[0] == val:
            self.Q.popleft()

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i, v in enumerate(nums):
            self.push(v)

            if i < k - 1:
                continue
            ans.append(self.Q[0])
            self.pop(nums[i - k + 1])
        return ans