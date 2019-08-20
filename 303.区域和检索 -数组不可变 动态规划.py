# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# 示例：
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 说明:
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法！！！！！！！！！
# 这句话很重要 这说明要保存 每次sum的状态 以免下次调用还要计算

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(1,len(nums)):
            nums[i] = nums[i]+nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        else:
            return self.nums[j]-self.nums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
