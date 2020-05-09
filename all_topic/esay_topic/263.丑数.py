class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 0
        while n <=30:
            if num % 2 ==0:
                num = num // 2
            elif num % 3 ==0:
                num = num //3
            elif num % 5 ==0:
                num = num //5
            else:
                break
            n += 1
        if num == 1:
            return True
        else:
            return False
a = Solution()
print(a.isUgly(6))