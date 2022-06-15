# encoding: utf-8
"""
@Project ：
@File: 890. 查找和替换模式 难度 中等  158.py
@Author: liuwz
@time: 2022/6/12 14:36
@desc: 
"""
from typing import List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

"""
你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。

如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。

（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）

返回 words 中与给定模式匹配的单词列表。

你可以按任何顺序返回答案。

 

示例：

输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
输出：["mee","aqq"]
解释：
"mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
"ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
因为 a 和 b 映射到同一个字母。
 

提示：

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            pattern_dict = {}
            word_dict = {}
            flag = True
            for i, s in enumerate(word):
                # s对应的pattern已存在
                if s in word_dict:
                    # 当前s对应pattern 和 已存在的不对应
                    if word_dict[s] != pattern[i]:
                        flag = False
                        break
                # s对应的pattern不存在
                else:
                    # s对应的pattern已被其他字符对应
                    if pattern[i] in pattern_dict and pattern[i] != s:
                        flag = False
                        break
                    word_dict[s] = pattern[i]
                    pattern_dict[pattern[i]] = s
            if flag:
                ans.append(word)
        return ans


a = Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")

