#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 11.盛最多水的容器_200418.py
@time: 2020/4/18 14:38
@desc: 
"""
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        Maximum = 0
        left = 0
        right = len(height) - 1
        # 双指针+dp
        while left < right:
            Maximum = max(Maximum, min(height[left], height[right]) * (right-left))
            # 判断左边或者是右边高度更小
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return Maximum


a = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(a)