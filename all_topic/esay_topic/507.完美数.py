#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 507.完美数.py
@time: 2020/4/7 16:16
@desc: 
"""
"""
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False
示例：
输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14

提示：
输入的数字 n 不会超过 100,000,000. (1e8)
"""


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        return sum(
            [item for inner in [[i, num / i] for i in range(2, int(math.sqrt(num)) + 1) if num % i == 0] for item in
             inner]) + 1 == num if num > 2 else False

        # import math
        # list_yinzi = [1]
        # if num <= 2:
        #     return False
        # for i in range(2, int(math.sqrt(num)) + 1):
        #     """
        #     为什么循环范围定在平方根呢？：因为一个数的因子是成对的，a=b*c。也就是说：找到一个因子b，肯定会找到相对应的另外一个因子c（a/b）。所以我们的工作量减少了一半。
        #     又有：一个因子变大，另一个因子必然要变小。假设b永远是小的那个，c是大的那个，那么b的最大值就是a的平方根。也就是b=c=(根号a)的时候。所以循环范围定在[1 , a的平方根+1]，+1的原因是为了能够取到a的平方根避免遗漏。
        #     """
        #     # 如果找到了一个因子，那么把其相对应的另一个因子一同加入到因子列表中
        #     if num % i == 0:
        #         list_yinzi.extend([i, num / i])
        #
        #     # 此处的set为了去重，因为会出现两个相同的平方根的情况。所以去掉重复
        #     # sorted重排序是因为，因子都是成对成对找出来的，也就是说一次找到的两个因子肯定会有一大一小。这样把所以因子找完放在一起，大小排序就乱了
        # return sum(list(set(list_yinzi))) == num

a = Solution().checkPerfectNumber(28)
print(a)

