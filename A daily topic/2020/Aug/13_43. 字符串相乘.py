#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 43. 字符串相乘.py
@time: 2020/8/13 10:47
@desc: 
"""
from typing import List
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""
#https://leetcode-cn.com/problems/multiply-strings/solution/bian-li-ji-yi-hua-by-hello_lwz/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # 暴力
        # nums1_length = len(num1)
        # nums2_length = len(num2)
        # ans = 0
        # for i in range(nums1_length - 1, -1, -1):
        #     for j in range(nums2_length - 1, -1, -1):
        #         ans += (int(num1[i]) * (10 ** (nums1_length - i - 1))) * (int(num2[j]) * (10 ** (nums2_length - j - 1)))
        # return str(ans)

        # 记忆化
        nums1_length = len(num1)
        nums2_length = len(num2)
        # 记录第一个数字字符串的不重复的每一位与第二个数字字符串的乘积
        # 格式 {第一个字符串的每一位不重复数字:[所处位数,最低位已经计算的乘积]}
        # 当遍历的数字已经在字典中出现，说明已经计算过这个数字与第二个字符串相乘的结果了，而不同的仅仅是位数不同！！也就是10的幂值不同
        # 我们要做的仅仅是根据 10**(当前数字所处的位置-字典中存储的最低位数字位数) 算出结果直接与当前已经累加的数字(ans)相加
        num_product = {}
        ans = 0
        for i in range(nums1_length - 1, -1, -1):
            if num1[i] in num_product:
                 ans += (10 ** ((nums1_length - i - 1) - num_product[num1[i]][0])) * num_product[num1[i]][1]
            else:
                old_ans = ans
                for j in range(nums2_length-1, -1, -1):
                    tmp_num = (int(num1[i]) * (10 ** (nums1_length - i - 1))) * (int(num2[j]) * (10 ** (nums2_length - j - 1)))
                    ans += tmp_num
                num_product[num1[i]] = [nums1_length - i - 1, ans - old_ans]
        return str(ans)


a = Solution().multiply("212315125","312312515")
print(a)