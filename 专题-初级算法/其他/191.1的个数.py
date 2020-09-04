# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
#
# 输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串00000000000000000000000000001011中，共有三位为'1'。

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n = bin(n)[2:]
        # sum = len([i for i in n if i == '1'])
        # return sum

        # n & n-1 可以将n的最低位的1变成0
        ans = 0
        while n > 0:
            n &= n - 1
            ans += 1
        return ans

a = Solution()
print(a.hammingWeight(2))