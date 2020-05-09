# 给定一个 32 位有符号整数，将整数中的数字进行反转。
# 示例 1:
# 输入: 123
# 输出: 321
# 示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
# 输入: 120
# 输出: 21
# 注意:
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。根据这
# 个假设，如果反转后的整数溢出，则返回 0。
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        x = str(x)
        if x[0]=="-":
            x = int("-"+ x[:0:-1])
            if x <-2**31 or x >2**31-1:
                return 0
            else:
                return x
        else:
            x = x[::-1]
            while True:
                if x[0] == "0":
                    x = x[1:]
                else:
                    break
            x = int(x)
            if x <-2**31 or x >2**31-1:
                return 0
            else:
                return x
a = Solution()
print(a.reverse(-120))

