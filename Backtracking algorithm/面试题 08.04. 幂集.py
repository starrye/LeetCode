#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题 08.04. 幂集.py
@time: 2020/4/25 17:49
@desc: 
"""
"""
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def travel_bak(tmp_list, selectable_nums):
            if len(tmp_list) <= len(nums):
                result.append(tmp_list[:])
            if len(tmp_list) == len(nums):
                return
            selectable_nums_tmp = selectable_nums
            for i in selectable_nums:
                if i in tmp_list:
                    continue
                selectable_nums_tmp = selectable_nums_tmp[1:]
                tmp_list.append(i)
                travel_bak(tmp_list, selectable_nums_tmp)
                tmp_list.pop()
        result = []
        travel_bak([], nums)
        return result


a = Solution().subsets([1,2,3])
print(a)
