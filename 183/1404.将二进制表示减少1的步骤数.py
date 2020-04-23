#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1404.将二进制表示减少1的步骤数.py
@time: 2020/4/23 10:57
@desc: 
"""
"""
给你一个以二进制形式表示的数字 s 。请你返回按下述规则将其减少到 1 所需要的步骤数：
如果当前数字为偶数，则将其除以 2 。
如果当前数字为奇数，则将其加上 1 。
题目保证你总是可以按上述规则将测试用例变为 1 。


示例 1：

输入：s = "1101"
输出：6
解释："1101" 表示十进制数 13 。
Step 1) 13 是奇数，加 1 得到 14 
Step 2) 14 是偶数，除 2 得到 7
Step 3) 7  是奇数，加 1 得到 8
Step 4) 8  是偶数，除 2 得到 4  
Step 5) 4  是偶数，除 2 得到 2 
Step 6) 2  是偶数，除 2 得到 1  
示例 2：

输入：s = "10"
输出：1
解释："10" 表示十进制数 2 。
Step 1) 2 是偶数，除 2 得到 1 
示例 3：

输入：s = "1"
输出：0

提示：

1 <= s.length <= 500
s 由字符 '0' 或 '1' 组成。
s[0] == '1'
"""


class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_num = int(s, 2)
        count = 0
        while s_num > 1:
            count += 1
            if not s_num % 2:
                s_num /= 2
            else:
                s_num += 1
        return count

        # s_num = 0
        # result = 0
        # for i in range(len(s)):
        #     s_num += int(s[::-1][i]) * (2 ** i)
        # while s_num != 1:
        #     result += 1
        #     if not s_num % 2:
        #         s_num /= 2
        #     else:
        #         s_num += 1
        # return result


# 1101 = 13
a = Solution().numSteps("1101")
print(a)