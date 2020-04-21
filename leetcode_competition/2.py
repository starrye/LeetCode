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
        # BFS
        # 传递次数
        transfer_number = 0
        global total
        # 方案数
        total = -1
        # 记录每一次所能到达的玩家编号
        next_player_ist = [0]
        # 0 --> n-1 的k轮传递方案
        relation.sort(key=lambda x: x[0])
        self.find_path(n, transfer_number, next_player_ist, relation, k)
        return total

    def find_path(self, n, transfer_number, next_player_ist, relation, k):
        next_new_list = []
        transfer_number += 1
        if transfer_number > k:
            # 超过要求传递次数则返回方案数，本轮可到达玩家编号中统计n-1的数量
            global total
            total = next_player_ist.count(n-1)
            return
        else:
            # 遍历本轮可到达玩家编号-->获取下轮可到达玩家编号
            for player in next_player_ist:
                for index, value in enumerate(relation):
                    if value[0] == player:
                        next_new_list.append(value[1])
            self.find_path(n, transfer_number, next_new_list, relation, k)


a = Solution().numWays(3,[[0,2],[0,1],[1,2],[2,1],[2,0],[1,0]],1)
print(a)