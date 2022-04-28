# encoding: utf-8
"""
@Project ： 
@File: 386.py
@Author: liuwz
@time: 2022/4/18 10:55 上午
@desc: 
"""
""":cvar
你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。

你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。

 

示例 1：

输入：n = 13
输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
示例 2：

输入：n = 2
输出：[1,2]
 

提示：

1 <= n <= 5 * 104
"""

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def cur(num):
            if num > n:
                return
            ans.append(num)
            for i in range(10):
                cur(num * 10 + i)
        for i in range(1, 10):
            cur(i)
        return ans

a = Solution().lexicalOrder(133)
