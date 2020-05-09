#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 5390.数青蛙.py
@time: 2020/4/20 14:00
@desc: 
"""
"""
给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 
中会混合多个 “croak” 。请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。
注意：要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。
如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。
示例 1：
输入：croakOfFrogs = "croakcroak"
输出：1 
解释：一只青蛙 “呱呱” 两次
示例 2：

输入：croakOfFrogs = "crcoakroak"
输出：2 
解释：最少需要两只青蛙，“呱呱” 声用黑体标注
第一只青蛙 "crcoakroak"
第二只青蛙 "crcoakroak"
示例 3：

输入：croakOfFrogs = "croakcrook"
输出：-1
解释：给出的字符串不是 "croak" 的有效组合。
示例 4：

输入：croakOfFrogs = "croakcroa"
输出：-1
"""


class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        """
        用一个字典统计五种字符的数量，合法的输入肯定满足前一个字符数量大于等于后一个字符数量
        即：count('c') >= count('r') >= count('o') >= count('a') >= count('k')
        某个时间点青蛙数量:'c'和'k'之间嵌套了多少个'c'
        即：count('c') - count('k')
        """
        if len(croakOfFrogs) % 5 != 0:
            return -1
        else:
            count_ = {'c':0,'r':0,'o':0,'a':0,'k':0}
            max_ = 0
            for i in croakOfFrogs:
                count_[i] += 1
                max_ = max(count_["c"] - count_["k"], max_)
                if count_['c'] < count_['r'] or count_['r'] < count_['o'] or count_['o'] < count_['a'] or count_['a'] < count_['k']:
                    return -1
            return max_


# a = Solution().minNumberOfFrogs("croakcroak")
# a = Solution().minNumberOfFrogs("crcoakroak")
# a = Solution().minNumberOfFrogs("croakcrook")
# a = Solution().minNumberOfFrogs("croakcroa")
# a = Solution().minNumberOfFrogs("aoocrrackk")
a = Solution().minNumberOfFrogs("crocakcroraoakk")
print(a)
