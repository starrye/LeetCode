#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 面试题 17.09. 第 k 个数.py
@time: 2020/6/24 16:47
@desc: 
"""
from typing import List
"""
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
示例 1:
输入: k = 5
输出: 9
"""


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
