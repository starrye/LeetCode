# encoding: utf-8
"""
@author: liuwz
@time: 2021/5/17 3:41 下午
@file: 换工位.py
@desc: 
"""

from typing import List
"""
因为要实施结对编程，想让两个员工的工位挨在一起：要求 [0,1] 员工坐在一起，[2, 3] 员工坐在一起，以此类推。不过挨着具体坐的位置并不重要，只要能挨在一起就可以了。
比如 [0, 1, 3, 2] 与 [2, 3, 1, 0] 都是满足要求的。现在给定一个数组 A[]，求换工位的最少次数，尽量让两个员工坐在一起。（给定 N 个员工，他们的编号总是 [0~N-1] ，并且 N 总是偶数）。

输入：A[] = [0, 3, 2, 1]
输出：1

解释：只需要换 1 次就可以了，比如，将 0 号员工与 2 号员工交换。
"""


class UF:
    def __init__(self, n):
        self.par = dict()
        self.ans = 0
        for i in range(n):
            # 初始化的时候就结成组 01 23 45 67...
            self.par[i] = i - (i&1)


    def find(self, x):
        if x == self.par[x]:
            return x

        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)
        if x_par != y_par:
            self.par[x_par] = y_par
            # 合并次数统计 即为想要接环的次数 反着推 你想要知道让两个数字挨着需要多少次交换 那就初始化的时候挨着需要多少次能够变成现在的情况
            self.ans += 1


class Solution:
    def exchange_station(self, A):
        n = len(A)
        uf = UF(n)

        for i in range(0, len(A), 2):
            uf.union(A[i], A[i+1])
        print(uf.par)
        return uf.ans


a = Solution().exchange_station([6, 4, 5, 2, 3, 7, 0, 1] )
print(a)