#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题 16.11. 跳水板.py
@time: 2020/7/8 10:25
@desc: 
"""
from typing import List
"""
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

示例：

输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}
提示：

0 < shorter <= longer
0 <= k <= 100000。
"""
import itertools
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        min_len = shorter * k
        if shorter == longer:
            return [min_len]
        # return [(shorter * (k - i) + longer * i) for i in range(k + 1)]
        result = [min_len]
        max_len = longer * k
        difference = longer - shorter
        # 等差数列 (shorter * (k - i) + longer * i) 等同于在上次的基础上去掉较短的 增加一个较长的 所以每次增加 (长-短)
        while min_len != max_len:
            min_len += difference
            result.append(min_len)
        return result


a = Solution().divingBoard(1,2,3)
print(a)