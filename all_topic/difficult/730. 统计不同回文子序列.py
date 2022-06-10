# encoding: utf-8
"""
@Project ： 
@File: 730. 统计不同回文子序列.py
@Author: liuwz
@time: 2022/6/10 2:11 PM
@desc: 
"""

import pandas as pd
import numpy as np
from typing import List
"""
给定一个字符串 s，返回 s 中不同的非空「回文子序列」个数 。

通过从 s 中删除 0 个或多个字符来获得子序列。

如果一个字符序列与它反转后的字符序列一致，那么它是「回文字符序列」。

如果有某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。

注意：

结果可能很大，你需要对 109 + 7 取模 。
 

示例 1：

输入：s = 'bccb'
输出：6
解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。
示例 2：

输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：共有 3104860382 个不同的非空回文子序列，104860361 对 109 + 7 取模后的值。
 

提示：

1 <= s.length <= 1000
s[i] 仅包含 'a', 'b', 'c' 或 'd'
"""

# f[i][j] 记为从i到j 一共有多少惠文串 最后返回f[0][n-1]
# 因为只有4个字母 先倒序 i 记录所有字符最左侧位置
# 然后从i 再正序 记录所有字符的最右侧位置 同时更新所有f[i][j]的数据
# 如何更新？
# 1/如果当前字母的左侧与右侧 相等 说明只含有一个字符 则+1
# 2/如果当前字母挨着 即 l+1=r 则说明 含有两个字符 但是只有2中情况 k or kk
# 3/如果其他情况 则 应该增加 f[l+1][r-1] + 2

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        mod = 10 ** 9 + 7
        f = [[0] * n for _ in range(n)]
        l = [-1] * 4
        for i in range(n-1, -1, -1):
            l[ord(s[i]) - 97] = i
            r = [-1] * 4
            for j in range(i, n):
                r[ord(s[j]) - 97] = j
                for k in range(4):
                    if l[k] == -1 or r[k] == -1:
                        continue
                    if l[k] == r[k]:
                        f[i][j] += 1
                    elif l[k] + 1 == r[k]:
                        f[i][j] += 2
                    else:
                        f[i][j] += f[l[k]+1][r[k]-1] + 2
            # print(f)
        return f[0][n-1] % mod


a = Solution().countPalindromicSubsequences("bccb")
print(a)