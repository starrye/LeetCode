#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 763. 划分字母区间.py
@time: 2020/7/28 11:29
@desc: 
"""
from typing import List
"""
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
示例 1：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # result = []
        # length = len(S)
        # i = 0
        # while i < length:
        #     # 更新右侧区间
        #     r_index = S.rfind(S[i])
        #     j = i
        #     while j < r_index:
        #         r_index = max(r_index, S.rfind(S[j]))
        #         j += 1
        #     result.append(r_index - i + 1)
        #     i = r_index + 1
        # return result

        # 没必要每次找最右侧元素的索引
        last = {v: k for k, v in enumerate(S)}
        start = end = 0
        res = []
        for k, v in enumerate(S):
            end = max(end, last[v])
            if k == end:
                res.append(end - start + 1)
                start = end + 1
        return res


a = Solution().partitionLabels("ababcbacadefegdehijhklij")
# b = Solution().partitionLabels("qiejxqfnqceocmy")
print(a)
# print(b)

