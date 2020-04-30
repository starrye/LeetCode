"""
编写一个算法来判断一个数 n 是不是快乐数。
快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。
示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution():
    def __init__(self):
        self.current_num = set()
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        for i, j in enumerate(str(n)):
            sum += int(j)**2
        if sum == 1:
            return True
        if sum in self.current_num:
            return False
        self.current_num.add(sum)
        return self.isHappy(sum)


a = Solution()
print(a.isHappy(13))


