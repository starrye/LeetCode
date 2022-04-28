# encoding: utf-8
"""
@Project ： 
@File: 440. 字典序的第K小数字.py
@Author: liuwz
@time: 2022/3/23 10:39 上午
@desc: 
"""

"""
给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。

 

示例 1:

输入: n = 13, k = 2
输出: 10
解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
示例 2:

输入: n = 1, k = 1
输出: 1
 

提示:

1 <= k <= n <= 109
"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        prefix = 1
        # 当前最小数字
        p = 1
        while p < k:
            cnt = self.get_count(prefix, n)
            # k位于当前层
            if p + cnt > k:
                # 进入当前层
                prefix *= 10
                p += 1
            else:
                prefix += 1
                p += cnt
        return prefix


    def get_count(self, prefix, n):
        """计算当前以prefix为前缀 有多少个数字"""
        # 对于字典序而言 + 1 > * 10
        cur = prefix
        next = prefix + 1
        count = 0
        while cur <= n:
            count += min(next, n+1) - cur
            cur *= 10
            next *= 10
        return count

a = Solution().findKthNumber(10, 3)
print(a)