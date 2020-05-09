class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num > 9:
            num1 = 0
            for i in str(num):
                num1 += int(i)
            num = num1
        return num
a = Solution()
print(a.addDigits(38))