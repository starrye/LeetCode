# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
# 示例 1:
# 输入: [3,0,1]
# 输出: 2

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1) // 2 - sum(nums)
a = Solution()
print(a.missingNumber([0,1,3,2,5]))