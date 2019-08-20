# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
# 示例 1:
# 输入: a = 1, b = 2
# 输出: 3
# 示例 2:
# 输入: a = -2, b = 3
# 输出: 1

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # if str(a)[0] == '-':
        #     a = bin(a)[3:]
        # b = bin(b)[2:]
        # sum = int(a)|int(b)
        # sum = int(str(sum), 2)
        # return sum
a = Solution()
print(a.getSum(-1,2))