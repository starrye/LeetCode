#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 5608. 完成所有任务的最少初始能量.py
@time: 2020/11/23 09:28
@desc: 
"""
from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key=lambda x:x[1]-x[0], reverse=True)
        print(tasks)
        if len(tasks) == 1:
            return tasks[0][1]

        ans = 0
        remainder = 0

        for actual, minimum in tasks:
            # 需要能量低于剩余能量
            if minimum <= remainder:
                remainder -= actual
            # 需要能量高于剩余能量，补充能量 到 需要能量的量
            else:
                # 需要补充能量到门槛量
                ans += minimum - remainder
                # 剩余能量变为 需求-实际
                remainder = minimum - actual


        return ans



a = Solution().minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]])
print(a)