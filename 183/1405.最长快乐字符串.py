#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1405.最长快乐字符串.py
@time: 2020/4/23 11:12
@desc: 
"""
"""
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。

 

示例 1：

输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。
示例 2：

输入：a = 2, b = 2, c = 1
输出："aabbc"
示例 3：

输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。
 

提示：

0 <= a, b, c <= 100
a + b + c > 0
"""


class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        # 贪心算法
        # 任何单一字符最大数量必须小于（另外两个字符+1）*2 如‘aabaabaacaa',b与c插入到a序列中，a的数量最多为8
        # 可用字母个数
        letter_dic = {"a": min(a, (b+c+1)*2), "b": min(b, (a+c+1)*2), "c": min(c, (a+b+1)*2)}
        result = ""
        for _ in range(sum(letter_dic.values())):
            tmp_letter_list = ["a","b","c"]
            if len(result) > 1 and result[-2] == result[-1]:
                tmp_letter_list.remove(result[-1])
            tmp= max(tmp_letter_list,key=lambda x:letter_dic[x])
            result += tmp
            letter_dic[tmp] -= 1
        return result



        # result = ""
        # while a + b + c > 0:
        #     if a == max(a, b, c):
        #         if result[-2:] != "aa":
        #             result += "a"
        #             a -= 1
        #         elif max(b,c) > 0:
        #             if b > c:
        #                 result += "b"
        #                 b -= 1
        #             else:
        #                 result += "c"
        #                 c -= 1
        #         else:
        #             return result
        #     elif b == max(a, b, c):
        #         if result[-2:] != "bb":
        #             result += "b"
        #             b -= 1
        #         elif max(a,c) > 0:
        #             if a > c:
        #                 result += "a"
        #                 a -= 1
        #             else:
        #                 result += "c"
        #                 c -= 1
        #         else:
        #             return result
        #     else:
        #         if result[-2:] != "cc":
        #             result += "c"
        #             c -= 1
        #         elif max(a,b) > 0:
        #             if a > b:
        #                 result += "a"
        #                 a -= 1
        #             else:
        #                 result += "b"
        #                 b -= 1
        #         else:
        #             return result
        # return result

a = Solution().longestDiverseString(1,1,7)
print(a)


