#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1443.py
@time: 2020/5/11 10:35
@desc: 
"""
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        all_edge = {}
        self.result = 0
        for i in edges:
            if str(i[0]) in all_edge.keys():
                all_edge[str(i[0])].append(str(i[1]))
            else:
                all_edge[str(i[0])] = []
                all_edge[str(i[0])].append(str(i[1]))
        all_par_node = all_edge.keys()
        def travel_back(tmp_node):
            for j in tmp_node:
                self.result += 1
                if j not in all_par_node:
                    if
                    continue
                travel_back(all_edge[j])
                if
        print(all_edge)
        travel_back(all_edge["0"])
        print(self.result)



a = Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False])
print(a)