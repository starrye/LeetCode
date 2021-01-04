#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 22.括号生成_200409.py
@time: 2020/4/9 10:05
@desc: 
"""
"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 定义返回结果
        res = []
        # 开始调用递归函数 深度搜索
        self.dps("", n, n, res)
        # 返回结果
        return res

    # 递归函数
    def dps(self, tmp, left, right, res):
        # 如果left == right == 0 表示此次递归完成
        if left == right == 0:
            res.append(tmp)
            return
        # 如果左括号数量大于右括号就返回 表示此组合不成效
        if left > right:
            return
        # 如果left 与 right 都有剩余 则递归
        if left:
            self.dps(tmp + "(", left-1, right, res)
        if right:
            self.dps(tmp + ")", left, right-1, res)


a = Solution().generateParenthesis(3)
print(a)