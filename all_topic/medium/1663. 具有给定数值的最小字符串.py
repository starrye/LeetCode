#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1663. 具有给定数值的最小字符串.py
@time: 2020/11/23 09:27
@desc: 
"""
from typing import List


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        i = 0
        array = ""
        while i < n:
            if (n-i-1) * 26 >= k:
                 array += "a"
                 i += 1
                 k -= 1
            else:
                print(array)
                print(k - (n-i-1))
                if i == k - 1:
                    array += chr(k - (n-i-1) + 96)
                    break
                else:
                    print(n - i - 1)
                    print(chr(k - (n-i-1)*26 + 96))
                    array += chr(k - (n-i-1)*26 + 96)
                i += 1
                while i < n:
                    array += "z"
                    i += 1
                break
        return array

a = Solution().getSmallestString(5, 73)
print(a)

