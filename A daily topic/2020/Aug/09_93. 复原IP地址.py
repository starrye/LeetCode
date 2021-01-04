#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 93. 复原IP地址.py
@time: 2020/11/2 13:56
@desc: 
"""
from typing import List
"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。


示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

提示：

0 <= s.length <= 3000
s 仅由数字组成
"""

# 回溯 长度最长为3，不能以0开头
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def help(temp_list, s):
            if len(temp_list) == 4:
                # 正好用完s串组成4个ip段
                if len(s) == 0:
                    result.append(".".join(temp_list))
                return
            # 每次选择可以选择 1 个 2 个 3个
            for i in range(min(3, len(s))):
                temp_num, remaining_num = s[:i+1], s[i+1:]
                # 判断当前剩余ip段的最大长度是否仍小于剩余s串
                # 则s串剩余则应该本次多选一个
                if (3 - len(temp_list)) * 3 < len(remaining_num):
                    continue
                # str(int(temp_num)) == temp_num 主要是判断开头是不是0开始
                if 0 <= int(temp_num) <= 255 and str(int(temp_num)) == temp_num:
                    help(temp_list + [temp_num], remaining_num)
        help([], s)
        return result

a = Solution().restoreIpAddresses("25525511135")
print(a)















