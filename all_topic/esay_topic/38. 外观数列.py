#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 38. 外观数列.py
@time: 2020/8/10 16:15
@desc: 
"""
from typing import List
"""
给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1

描述前一项，这个数是 1 即 “一个 1 ”，记作 11

描述前一项，这个数是 11 即 “两个 1 ” ，记作 21

描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211

描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

 

示例 1:

输入: 1
输出: "1"
解释：这是一个基本样例。
示例 2:

输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。
"""

"""
每次外循环含义为给定上一个人报的数，求下一个人报的数
每次内循环为遍历上一个人报的数

先设置上一人为'1'
开始外循环
每次外循环先置下一人为空字符串，置待处理的字符num为上一人的第一位，置记录出现的次数为1
开始内循环，遍历上一人的数，如果数是和num一致，则count增加。
若不一致，则将count和num一同添加到next_person报的数中，同时更新num和count
别忘了更新next_person的最后两个数为上一个人最后一个字符以及其出现次数！

作者：qsctech-sange
链接：https://leetcode-cn.com/problems/count-and-say/solution/ji-su-jie-bu-di-gui-zhi-ji-lu-qian-hou-liang-ren-p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # 设置初始值
        pre_str = "1"
        for i in range(1, n):
            cur_str, count, tmp_str = "", 1, pre_str[0]
            for j in pre_str[1:]:
                if j == tmp_str:
                    count += 1
                else:
                    cur_str += str(count) + tmp_str
                    count = 1
                    tmp_str = j
            cur_str += str(count) + tmp_str
            pre_str = cur_str
        return pre_str

a = Solution().countAndSay(3)
print(a)