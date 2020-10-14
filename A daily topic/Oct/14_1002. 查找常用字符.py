#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1002. 查找常用字符.py
@time: 2020/10/14 11:29
@desc: 
"""
from collections import Counter
from typing import List
"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。


示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]
 

提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母
"""
from functools import reduce
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """
        reduce() 函数会对参数序列中元素进行累积。函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
        用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果
        :param A:
        :return:
        """
        return list(reduce(lambda x, y:x & y, map(Counter, A)).elements())

        # ans = []
        # min_char = min(A, key=len)
        # for char in min_char:
        #     if all(char in i for i in A):
        #         ans.append(char)
        #         A = [i.replace(char, "", 1) for i in A]
        # return ans


a = Solution().commonChars(["bella","label","roller"])
print(a)