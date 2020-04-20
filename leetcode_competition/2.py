#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 2.py
@time: 2020/4/18 14:57
@desc: 
"""
class Solution(object):
    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """
        transfer_number = 0
        global total
        total = -1
        next_list = [0]
        # 0 --> n-1 的k轮传递方案
        relation.sort(key=lambda x: x[0])
        self.find_path(n, transfer_number, next_list, relation, k)
        return total

    def find_path(self, n, transfer_number, next_list, relation, k):
        next_new_list = []
        transfer_number += 1
        if transfer_number > k:
            global total
            total = next_list.count(4)
            return
        else:
            for va in next_list:
                for index, value in enumerate(relation):
                    if value[0] == va:
                        next_new_list.append(value[1])
            self.find_path(n, transfer_number, next_new_list, relation, k)


a = Solution().numWays(3, [[0,2],[2,1]], 2)
print(a)