# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 46. 把数字翻译成字符串.py
@Author: liuwz
@time: 2022/1/6 6:12 下午
@desc: 
"""

"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231
"""
class Solution:
    def translateNum(self, num: int) -> int:
        n_str = str(num)
        n = len(n_str)
        dp = [1] * n
        for i in range(1, n):
            n_int = int(n_str[i-1:i+1])
            if 25 >= n_int >= 10:
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[-1]


a = Solution().translateNum(18580)
print(a)
                