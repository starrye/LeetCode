#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 5393.可获得的最大点数.py
@time: 2020/4/26 10:30
@desc: 
"""

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        # 两边滑窗 总数不变 左边+1 右边-1
        # 从右侧选k个值开始
        left_sum = 0
        right_sum = sum(cardPoints[-k:])
        result = left_sum + right_sum
        for i in range(k):
            left_sum += cardPoints[i]
            right_sum -= cardPoints[-k+i]
            result = max(result, left_sum + right_sum)
        return result

        # if k >= len(cardPoints):
        #     return sum(cardPoints)
        # i = 0
        # max_sum = 0
        # j = len(cardPoints)-1
        # left_max = sum(cardPoints[:k])
        # right_max = sum(cardPoints[-k:])
        # left_chose_count = 0
        # right_chose_count = 0
        # while left_chose_count+right_chose_count < k:
        #     if left_max >= right_max:
        #         max_sum += cardPoints[i]
        #         left_max -= cardPoints[i]
        #         i += 1
        #         right_max -= cardPoints[-k+right_chose_count]
        #         right_chose_count += 1
        #     else:
        #         max_sum += cardPoints[j]
        #         right_max -= cardPoints[j]
        #         left_max -= cardPoints[k-1-left_chose_count]
        #         left_chose_count += 1
        #         j -= 1
        #
        #
        # return max_sum


a = Solution().maxScore([100,40,17,9,73,75],5)
# b = Solution().maxScore([11,49,100,20,86,29,72],4)
print(a==305)
# print(b==232)