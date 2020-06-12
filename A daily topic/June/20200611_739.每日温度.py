#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 739.每日温度.py
@time: 2020/4/11 17:20
@desc: 
"""
"""
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 栈的利用
        result = [0] * len(T)
        stack = []
        for index, value in enumerate(T):
            # 栈为空 或者 当前元素 小于等于 栈的最上方元素 --> 当前元素携带索引入栈
            if not stack or value <= stack[-1][1]:
                stack.append([index, value])
            else:
                while True:
                    # 不停取出栈的最上方元素与当前元素对比，当前元素较大则存放索引差到result中并弹出最上方元素，反之则携带索引入栈
                    if stack:
                        pre_T = stack[-1][1]
                        if pre_T < value:
                            result[stack[-1][0]] = index - stack[-1][0]
                            stack.pop()
                        else:
                            stack.append([index, value])
                            break
                    else:
                        stack.append([index, value])
                        break
        return result


a = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(a)