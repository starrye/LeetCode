#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 605. 种花问题.py
@time: 2020/5/10 14:59
@desc: 
"""
from typing import List

"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:

数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        i = 0
        length = len(flowerbed) - 1
        while i <= length:
            if i == length:
                if flowerbed[i] == 0:
                    n -= 1
                break
            if flowerbed[i] == flowerbed[i+1] == 0:
                n -= 1
                if n == 0:
                    return True
                i += 2
                continue
            elif flowerbed[i] == 1:
                i += 2
                continue
            elif flowerbed[i+1] == 1:
                i += 3
                continue
        return n == 0

a = Solution().canPlaceFlowers([1,0,0,0,1,0,0],2)
b = Solution().canPlaceFlowers([1,0,0,0,1],1)
c = Solution().canPlaceFlowers([0,0,1,0,0],1)
e = Solution().canPlaceFlowers([1],1)
print(a)
print(b)
print(c)
print(e)