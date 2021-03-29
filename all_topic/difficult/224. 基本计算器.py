# encoding: utf-8
"""
@author: liuwz
@time: 2021/3/29 2:38 下午
@file: 224. 基本计算器.py
@desc: 
"""
"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
示例 1：
输入：s = "1 + 1"
输出：2
示例 2：

输入：s = " 2-1 + 2 "
输出：3
示例 3：

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
 

提示：

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def calculate(self, s: str) -> int:
        """
        res: 保存随时计算的结果
        num：保存当前数值
        sign：保存当前数值前的符号 如果是 - 则当前数值乘-1 否则就是乘1 这里主要为了方便计算时都是使用加号
        """
        res, num, sign = 0, 0, 1
        stack = []
        for i in s:
            if i.isdigit():
                # 字符串转化为数字的常用方法
                num = num * 10 + int(i)
            elif i == "+" or i == "-":
                # 假设当前- 出现在第一位 则res = 0 num = 0 sign = -1
                # 假设当前- 出现在中间一位，则res 计算前序结果 然后将 sign 变化为1或者-1 然后num=0方便后面的数字转化
                res += sign * num
                sign = 1 if i == "+" else -1
                num = 0
            elif i == "(":
                # 当前字符串为( 则将前面的res 和 sign入栈 是因为括号内的计算优先级高，将res 和 sign重新初始化计算括号内的res
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif i == ")":
                # 当前字符为 ） 则计算res 并 将前面入栈的res 和 sign 出栈并计算
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        res += sign * num
        return res