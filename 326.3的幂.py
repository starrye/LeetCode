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
        while n >= 3:
            if n % 3 != 0:
                return False
            n = n / 3
        return False if n != 1 else True