# encoding: utf-8
"""
@Project ：
@File: 668. 乘法表中第k小的数.py
@Author: liuwz
@time: 2022/5/18 10:35
@desc: 
"""
""":cvar
几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？

给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

例 1：

输入: m = 3, n = 3, k = 5
输出: 3
解释: 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
例 2：

输入: m = 2, n = 3, k = 6
输出: 6
解释: 
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).
注意：

m 和 n 的范围在 [1, 30000] 之间。
k 的范围在 [1, m * n] 之间。
"""

# 1/二分查找一个数字
# 2/针对这个数字 查看所有比它小的数字的数量（左下角、或者右上角开始）
# 3/如果数量<k 则表示 应该l=mid+1查找下一个数字 并进行2-3 or 2-4循环
# 4/如果数量>k 则表示 应该r=mid查找下一个数字 并进行2-3 or 2-4循环


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        i, j = 1, m*n
        while i < j:
            mid = i + (j-i) // 2
            num = self.cnt(m, n, mid)
            # print(mid, num)
            if num >= k:
                j = mid
            else:
                i = mid + 1
        return i

    def cnt(self, m, n, mid):
        cnt, i, j = 0, m, 1
        while i >= 1 and j <= n:
            if i*j > mid:
                i -= 1
            else:
                cnt += i
                j += 1
        return cnt


a = Solution().findKthNumber(2, 3, 5)
print(a)


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        for i in range(1, len(words)):
            if words[i] != words[i+1].Count():
                ans.append(words[i])
        return ans