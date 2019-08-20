# 输入: 19
# 输出: true
# 解释:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution:
    result = []
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        for i,j in enumerate(str(n)):
            sum += int(j)**2
        if sum == 1:
            return True
        if sum in Solution.result:
            return False
        Solution.result.append(sum)
        return self.isHappy(sum)
a = Solution()
print(a.isHappy(10))


