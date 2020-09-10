#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 39. 组合总和.py
@time: 2020/9/9 09:51
@desc: 
"""
from typing import List
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
] 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates = sorted(candidates)
        result = []
        # 标准回溯
        def help(current_list, start):
            current_sum = sum(current_list)
            if current_sum == target:
                result.append(current_list[:])
            elif current_sum > target:
                return
            else:
                for i in range(start, len(candidates)):
                    if candidates[i] > target:
                        return
                    current_list.append(candidates[i])
                    help(current_list, i)
                    current_list.pop()
        help([], 0)
        return result

        # 优化回溯-
        # def help(current_list, start, target):
        #     for i in range(start, len(candidates)):
        #         if candidates[i] > target:
        #             return
        #         elif candidates[i] == target:
        #             result.append(current_list + [candidates[i]])
        #         else:
        #             help(current_list + [candidates[i]], i, target - candidates[i])
        # help([], 0, target)
        # return result

a = Solution().combinationSum([2,3,5, 1], 8)
print(a)
