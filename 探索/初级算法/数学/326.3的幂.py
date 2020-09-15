# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
# 示例 1:
#
# 输入: 27
# 输出: true

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # while n >= 3:
        #     if n % 3 != 0:
        #         return False
        #     n = n / 3
        # return False if n != 1 else True

        """
        3的幂次的质因子只有3，而所给出的n如果也是3的幂次，
        故而题目中所给整数范围内最大的3的幂次的因子只能是3的幂次，1162261467是3的19次幂，是整数范围内最大的3的幂次
        """
        return n > 0 and 1162261467 % n == 0;