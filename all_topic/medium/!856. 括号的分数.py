#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 856. 括号的分数.py
@time: 2020/5/22 16:25
@desc: 
"""
from typing import List
"""
给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

() 得 1 分。
AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
(A) 得 2 * A 分，其中 A 是平衡括号字符串。
 

示例 1：

输入： "()"
输出： 1
示例 2：

输入： "(())"
输出： 2
示例 3：

输入： "()()"
输出： 2
示例 4：

输入： "(()(()))"
输出： 6
 

提示：

S 是平衡括号字符串，且只含有 ( 和 ) 。
2 <= S.length <= 50
"""


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        """
        栈存当前分数
        当( 时 栈.append(0)
        当）时 v = 栈.pop() 然后以2*v的结果累加到上层也就是栈[-1]上面
        考虑（）情况 栈[-1]应该取 max(1,2*v)
        """
        stack = [0]
        for i in S:
            if i == "(":
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] = max(1, v * 2)
        return stack[-1]

a = Solution().scoreOfParentheses("((()))")
print(a)
