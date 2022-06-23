# encoding: utf-8
"""
@Project ： 
@File: 30. 串联所有单词的子串.py
@Author: liuwz
@time: 2022/6/23 11:02
@desc: 
"""
from collections import defaultdict

import pandas as pd
import numpy as np
from typing import List

"""
给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
示例 3：

输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
 

提示：

1 <= s.length <= 104
s 由小写英文字母组成
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] 由小写英文字母组成
"""


# words单词长度一致(按照固定长度划分子串)，不需要考虑words单词串联的顺序(只要数量对应上即可)

# 1/words总长度统计出来，即单词个数*单词数量 并统计每个单词出现的次数
# 2/在s中以滑动窗口(窗口大小为words总长度)的形式枚举每一个子串
# 3/窗口里面的字符串 以 words单个单词长度做切割，然后判断出现次数和words中是否一致,若不一致及时break , 一致则将窗口初始位置保存
# 4/返回结果


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # w_s_len, w_len = len(words), len(words[0])
        # i, j = 0, w_s_len * w_len - 1
        # # count_words = Counter(words)
        # words_dict = defaultdict(int)
        # for word in words:
        #     words_dict[word] += 1
        # ans = []
        # while j < len(s):
        #     sub_s = s[i:j+1]
        #     temp_dict = words_dict.copy()
        #     match = True
        #     for k in range(0, len(sub_s), w_len):
        #         if sub_s[k:k+w_len] in temp_dict and temp_dict[sub_s[k:k+w_len]] != 0:
        #             temp_dict[sub_s[k:k+w_len]] -= 1
        #         else:
        #             match = False
        #             break
        #         # temp.append(sub_s[k:k+w_len])
        #     # if count_words == Counter(temp):
        #         # ans.append(i)
        #     if match:
        #         ans.append(i)
        #     i += 1
        #     j += 1
        # return ans

        s_len, w_s_len, w_len = len(s), len(words), len(words[0])
        word_len = w_s_len * w_len - 1
        words_dict = defaultdict(int)
        for word in words:
            words_dict[word] += 1
        ans = []
        for i in range(s_len - word_len):
            sub_s = s[i:i + word_len + 1]
            temp_dict = words_dict.copy()
            match = True
            for j in range(0, word_len + 1, w_len):
                # print(sub_s[j:j+w_len])
                if sub_s[j:j + w_len] in temp_dict and temp_dict[sub_s[j:j + w_len]] != 0:
                    temp_dict[sub_s[j:j + w_len]] -= 1
                else:
                    match = False
                    break
            if match:
                ans.append(i)
        return ans


