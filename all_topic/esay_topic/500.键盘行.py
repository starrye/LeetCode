#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 500.键盘行.py
@time: 2020/4/7 15:24
@desc: 
"""
"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
示例：

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 利用python判断一个集合是否是另一个集合的子集，issubset函数
        return [i for i in words if set(i.lower()).issubset(set("qwertyuiop")) or set(i.lower()).issubset(set("asdfghjkl")) or set(i.lower()).issubset(set("zxcvbnm"))]

        # new_line = []
        # first_line = "qwertyuiop"
        # second_line = "asdfghjkl"
        # third_line = "zxcvbnm"
        # for word in words:
        #     word_set = set(word.lower())
        #     if word_set.issubset(set(first_line)) or word_set.issubset(set(second_line)) or word_set.issubset(set(third_line)):
        #         new_line.append(word)
        # return new_line


a = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
print(a)