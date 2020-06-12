#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1.py
@time: 2020/5/10 10:29
@desc: 
"""
from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        tmp_index = 0
        length = len(target)
        for i in range(1,n+1):
            if tmp_index == length:
                return result
            if target[tmp_index] == i:
                result.append("Push")
                tmp_index += 1
            else:
                result.extend(["Push", "Pop"])
        return result

a = Solution().buildArray([2,3],1)
b = Solution().buildArray([1,2,3],3)
c = Solution().buildArray([1,2],4)
d = Solution().buildArray([2,3,4],4)
print(a)
print(b)
print(c)
print(d)