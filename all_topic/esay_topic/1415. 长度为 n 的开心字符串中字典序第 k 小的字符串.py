#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1415. 长度为 n 的开心字符串中字典序第 k 小的字符串.py
@time: 2020/4/20 17:20
@desc: 
"""
"""
一个 「开心字符串」定义为：
仅包含小写字母 ['a', 'b', 'c'].
对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。
比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc" 都不是开心字符串。
给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。
请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。
示例 1：

输入：n = 1, k = 3
输出："c"
解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。
示例 2：

输入：n = 1, k = 4
输出：""
解释：长度为 1 的开心字符串只有 3 个。
示例 3：

输入：n = 3, k = 9
输出："cab"
解释：长度为 3 的开心字符串总共有 12 个 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"] 。第 9 个字符串为 "cab"
示例 4：
输入：n = 2, k = 7
输出：""
示例 5：
输入：n = 10, k = 100
输出："abacbabacb"
1 <= n <= 10
1 <= k <= 100
"""


class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 回溯算法
        self.res = ""
        self.n = n
        self.k = k
        # dfs生成开心字符串 出口为字符串长度==n
        def dfs(cur, tmp):
            if len(cur) == self.n:
                self.k -= 1
                if self.k == 0:
                    self.res = cur
                    return
                return
            for i in tmp:
                if self.res:
                    return self.res
                new_tmp = [j for j in ["a", "b", "c"] if j != i]
                dfs(cur+i, new_tmp)
        dfs("", ["a", "b", "c"])
        return self.res
        #return self.res[k-1] if k -1 < len(self.res) else ''

    #     # 初始化值
    #     self.result = ''
    #     self.n = n
    #     self.k = k
    #     # 生成开心字符串
    #     self.get_happy("a")
    #     self.get_happy("b")
    #     self.get_happy("c")
    #     return self.result
    #
    # def get_happy(self, s):
    #     # 长度等于n的长度跳出循环
    #     if len(s) == self.n:
    #         # k -1 当k=0即为想要的第k个开心字符串
    #         self.k -= 1
    #         if self.k == 0:
    #             self.result = s
    #         return
    #     # 如果前一个字母不为 a 则加a
    #     if s[-1] != "a":
    #         self.get_happy(s+'a')
    #     # 如果前一个字母不为 b 则加b
    #     if s[-1] != "b":
    #         self.get_happy(s+'b')
    #     # 如果前一个字母不为 c 则加c
    #     if s[-1] != "c":
    #         self.get_happy(s+'c')


a = Solution().getHappyString(2,3)
print(a)


