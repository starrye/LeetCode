class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not n % 4 == 0
a = Solution()
print(a.canWinNim(1))