# encoding: utf-8
"""
@author: liuwz
@time: 2021/3/29 2:36 下午
@file: 84. 柱状图中最大的矩形.py
@desc: 
"""
"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。


图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

 

示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        单调递增栈，循环柱子 假设到i(索引)，
        1/这根柱子比栈顶柱子A(索引)更小，则往外弹栈A的同时计算以弹出的那根柱子heights[A]为高 以 i - A 为底 计算面积
        2/继续与栈顶柱子高度对比，直到找不到比他更小的柱子，则把他入栈
        3/栈的最后要添加一个高度为0的柱子 目的是弹出栈内所有柱子

        示例：
        1/ 高度为2的柱子索引0入栈
        2/ 高度为1的柱子索引1入栈，比2小，则弹出索引0 高度为2 宽度为 1-0 = 1 则此时最大面积为2
        3/ 高度为5的柱子索引2入栈，比1大，无变动
        4/ 高度为6的柱子索引3入栈，比5大，无变动
        5/ 高度为2的柱子索引4入栈，比6小，则弹出索引3 高度为6 宽度为4-3 = 1 则此时最大面积为6，
             继续与栈顶元素对比   比5小，则弹出索引2 高度为5 宽度为4-2 = 2 则此时最大面积为10
             继续与栈顶元素对比   比2大 无变动
        6/ 高度为3的柱子索引5入栈，比2大，无变动
        7/ 高度为0的柱子索引6入栈，比5小，则弹出索引5 高度为3 宽度为6-5 = 1 则此时最大面积为MAX(10, 3)=10
             继续与栈顶元素对比   比2小，则弹出索引4 高度为2 宽度为6-4 = 2 则此时最大面试为MAX(10, 2*2)=10
             继续与栈顶元素对比   比1小，则弹出索引1 高度为1 宽度为6(栈内没有元素 则采用当前元素索引，说明弹出的这个元素是最小的柱子) 则此时最大面积为MAX(10, 6)=10
             高度计算：heights[stack.pop()]
             宽度计算：((index - stack[-1] - 1) if stack else index)
        """
        heights.append(0)
        stack = []
        max_area = 0
        for index, value in enumerate(heights):
            while stack and value < heights[stack[-1]]:
                max_area = max(max_area, heights[stack.pop()] * ((index - stack[-1] - 1) if stack else index))
            stack.append(index)
        return max_area