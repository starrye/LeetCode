#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 659. 分割数组为连续子序列.py
@time: 2020/12/4 09:41
@desc: 
"""
from typing import List

"""
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
如果可以完成上述分割，则返回 true ；否则，返回 false 。

示例 1：
输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 : 
1, 2, 3
3, 4, 5

示例 2：
输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 : 
1, 2, 3, 4, 5
3, 4, 5


示例 3：
输入: [1,2,3,4,4,5]
输出: False

提示：
输入的数组长度范围为 [1, 10000]
"""

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # counter 保存nums数组每个元素的出现次数
        # end 保存以每个元素结尾的连续数组的个数
        # 瞻前顾后！没有适合我的队伍 我就自己拉两个人组队！ 找不到人那GG
        counter, end = {}, {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        for j in nums:
            # 当前元素有剩余
            if counter[j] > 0:
                # 有以j-1元素结尾的连续数组则直接吧j挂到后面
                if end.get(j - 1, 0) > 0:
                    end[j-1] -= 1
                    end[j] = end.get(j, 0) + 1
                    counter[j] -= 1
                else:
                    # 新创建以j为开头的连续数组个数 判断后面两个数是否存在
                    if counter.get(j+1, 0) and counter.get(j+2, 0):
                        end[j+2] = end.get(j+2, 0) + 1
                        counter[j] -= 1
                        counter[j+1] -= 1
                        counter[j+2] -= 1
                    else:
                        return False
        return True

        # 暴力
        # result = []
        # for i in nums:
        #     for v in result:
        #         if i == v[-1] + 1:
        #             v.append(i)
        #             break
        #     else:
        #         result.insert(0, [i])
        # return all([len(v) >= 3 for v in result])


a = Solution().isPossible([1, 2, 3, 4, 5])
print(a)