#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 415.字符串相加.py
@time: 2019/11/23 20:36
@desc: 
"""
"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
"""

class Solution():
    def addStrings(self, num1, num2) -> str:

        max_num,min_num = ([ord(i)-48 for i in num1], [ord(j) - 48 for j in num2]) if len(num1) > len(num2) else \
            ([ord(i) - 48 for i in num2], [ord(j) - 48 for j in num1])
        carry = 0
        for i in range(-1, -len(min_num)-1, -1):
            max_num[i] += min_num[i] + carry
            if max_num[i] >= 10:
                max_num[i] -= 10
                carry = 1
            else:
                carry = 0
        if not carry:
            return ''.join(str(i) for i in max_num)
        for i in range(-len(min_num)-1, -len(max_num)-1, -1):
            max_num[i] += carry
            if max_num[i] >= 10:
                max_num[i] -= 10
                carry = 1
            else:
                return ''.join(str(i) for i in max_num)
        return '1' + ''.join(str(i) for i in max_num)

a = Solution().addStrings('12345', '12345')
print(a)