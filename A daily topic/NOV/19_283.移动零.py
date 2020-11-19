# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[count] = nums[i]
        #         count += 1
        # for i in range(count,len(nums)):
        #     nums[i] = 0

        # double pointer
        i = j = 0
        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] == 0:
                i += 1
            while j < len(nums) and nums[j] != 0 and j < i:
                j += 1
            if i < len(nums) and j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
a = Solution()
print(a.moveZeroes([1,0,0,2,0,4,2,0]))