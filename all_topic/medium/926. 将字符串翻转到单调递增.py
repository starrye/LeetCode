# encoding: utf-8
"""
@Project ：
@File: 926. 将字符串翻转到单调递增.py
@Author: liuwz
@time: 2022/6/11 14:18
@desc: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

"""
如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。

给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。

返回使 s 单调递增的最小翻转次数。

 

示例 1：

输入：s = "00110"
输出：1
解释：翻转最后一位得到 00111.
示例 2：

输入：s = "010110"
输出：2
解释：翻转得到 011111，或者是 000111。
示例 3：

输入：s = "00011000"
输出：2
解释：翻转得到 00000000。
 

提示：

1 <= s.length <= 105
s[i] 为 '0' 或 '1'
"""

# 1-> 后面如果是0 就变0(贪心)
#  -> 后面如果是1  应该看后面0多还是1多  如果1多或相等 则返回后面0的数量  如果0多 直接+后面1的数量+当前1返回
#

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        one_count = 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == "1":
                one_count += 1
                dp[i] = dp[i - 1]
            else:
                # 考虑将 0变为 1 或者 把前面的1都变为0
                dp[i] = min(dp[i - 1] + 1, one_count)
        return dp[-1]


a = Solution().minFlipsMonoIncr("0101100011")
print(a)
