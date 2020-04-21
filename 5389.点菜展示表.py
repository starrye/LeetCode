#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 5389.点菜展示表.py
@time: 2020/4/20 11:13
@desc: 
"""
"""
给你一个数组 orders，表示客户在餐厅中完成的订单，确切地说， orders[i]=[customerNamei,tableNumberi,foodItemi] ，
其中 customerNamei 是客户的姓名，tableNumberi 是客户所在餐桌的桌号，而 foodItemi 是客户点的餐品名称。
请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，
后面每一列都是按字母顺序排列的餐品名称。接下来每一行中的项则表示每张餐桌订购的相应餐品数量，
第一列应当填对应的桌号，后面依次填写下单的餐品数量。

注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。

示例 1：

输入：orders = [["David","3","Ceviche"],
["Corina","10","Beef Burrito"],
["David","3","Fried Chicken"],
["Carla","5","Water"],
["Carla","5","Ceviche"],
["Rous","3","Ceviche"]]
输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
       ["3","0","2","1","0"],
       ["5","0","1","0","1"],
       ["10","1","0","0","0"]] 
"""


class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        # 获取菜单列表并排序
        table_first_info = sorted(list(set([i[2] for i in orders])))
        # 创建第一行数据
        table_first_info.insert(0,"Table")
        result = []
        result.append(table_first_info)
        # 已写入结果的桌号
        table_marked = []
        # 表中的数据行应该按餐桌桌号升序排列
        orders.sort(key=lambda x:int(x[1]))
        for order in orders:
            if order[1] not in table_marked:
                table_marked.append(order[1])
                # 创建当前行数据
                order_current = ["0"]*len(table_first_info)
                order_current[0] = order[1]
                # 菜+1
                order_current[table_first_info.index(order[2])] = str(int(order_current[table_first_info.index(order[2])]) + 1)
                result.append(order_current)
            else:
                # 获取已有的订单行  获取到菜品 + 1
                result[table_marked.index(order[1])+1][table_first_info.index(order[2])] = str(int(result[table_marked.index(order[1])+1][table_first_info.index(order[2])])+1)
        return result


a = Solution().displayTable([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]])
print(a)