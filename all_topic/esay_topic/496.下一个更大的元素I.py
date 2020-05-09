#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 496.下一个更大的元素I.py
@time: 2020/4/7 11:03
@desc: 
"""
"""
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
注意:
nums1和nums2中所有元素是唯一的。
nums1和nums2 的数组大小都不超过1000。
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stk, d = [], {}
        for c in nums2:
            while stk and stk[-1] < c:
                # 倒序获取到小于当前数的元素
                t = stk.pop()
                # key为当前数 value为大于该数的下一个元素
                d[t] = c
            stk.append(c)
        ans = []
        for i in nums1:
            ans.append(d.get(i, -1))
        return ans


        # new_nums = []
        # for i in nums1:
        #     new_nums2 = nums2[nums2.index(i)+1:]
        #     if not new_nums2:
        #         new_nums.append(-1)
        #         continue
        #     else:
        #         for j in new_nums2:
        #             if j > i:
        #                 new_nums.append(j)
        #                 break
        #         else:
        #             new_nums.append(-1)
        # return new_nums


a = Solution().nextGreaterElement([4,1,2],[1,3,3,2,4])
print(a)