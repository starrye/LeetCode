# encoding: utf-8
"""
@Project ： 
@File: 473. 火柴拼正方形.py
@Author: liuwz
@time: 2022/6/1 10:53 AM
@desc: 
"""
from functools import lru_cache

import pandas as pd
import numpy as np
from typing import List

"""
你将得到一个整数数组 matchsticks ，其中 matchsticks[ms_index] 是第 ms_index 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。

如果你能使这个正方形，则返回 true ，否则返回 false 。

 

示例 1:



输入: matchsticks = [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。
示例 2:

输入: matchsticks = [3,3,3,3,4]
输出: false
解释: 不能用所有火柴拼成一个正方形。
 

提示:

1 <= matchsticks.length <= 15
1 <= matchsticks[ms_index] <= 108
"""

# 1/由于每根火柴都需要用上，所以首先判断火柴棍的长度和是否是4的倍数，同时判断最长的火柴是否超过了边长(总和/4)
# 2/使用a,b,c,d记录四边的边长， 开始递归进行判断
# 3/注意剪纸


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchstick_len = sum(matchsticks)
        if matchstick_len % 4:
            return False
        matchsticks.sort()
        side_len = matchstick_len // 4
        if matchsticks[-1] > side_len:
            return False
        # side_list = [0, 0, 0, 0]

        @lru_cache(None)
        # def dfs(side_list, ms_index):
        def dfs(a, b, c, d, ms_index):
            print(ms_index)
            # if ms_index == len(matchsticks) and side_list[0] == side_list[-1] == side_len:
            if ms_index == len(matchsticks) and a == b == c == d == side_len:
                return True
            res = False
            # for ms_index, side in enumerate(side_list):
            #     if side + matchsticks[ms_index] <= side_len:
            #         side_list[ms_index] += matchsticks[ms_index]
            #         res = res or dfs(side_list, ms_index + 1)
            if a + matchsticks[ms_index] <= side_len:
                res = res or dfs(a + matchsticks[ms_index], b, c, d, ms_index + 1)
            if b + matchsticks[ms_index] <= side_len:
                res = res or dfs(a, b + matchsticks[ms_index], c, d, ms_index + 1)
            if c + matchsticks[ms_index] <= side_len:
                res = res or dfs(a, b, c + matchsticks[ms_index], d, ms_index + 1)
            if d + matchsticks[ms_index] <= side_len:
                res = res or dfs(a, b, c, d + matchsticks[ms_index], ms_index + 1)
            
            return res
        ans = dfs(0, 0, 0, 0, 0)
        return ans

a = Solution().makesquare([3,2,3,2,2,3,1,4])
print(a)