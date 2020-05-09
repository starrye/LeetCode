#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 520.检测大写字母.py
@time: 2020/4/7 17:40
@desc: 
"""
"""
给定一个单词，你需要判断单词的大写使用是否正确。
我们定义，在以下情况时，单词的大写用法是正确的：
全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。
示例 1:
输入: "USA"
输出: True
示例 2:
输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。

"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: boolw
        """
        # islower 检测 单词是否全部是小写
        # istitle 检测 单词是否仅首字母是大写，其他是小写  简化为 word[0].isupper and word[1:].islower 时间缩短
        # isupper 检测 单词是否全部是大写
        # return word.islower() or (word[0].isupper() and word[1:].islower()) or word.isupper()

        return True if word[1:].islower() or word.isupper() or (len(word)==1 and word.islower()) else False


a = Solution().detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf")
print(a)