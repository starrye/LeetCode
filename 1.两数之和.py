# 给定一个整数数组和一个目标值,找出数组中和为目标值得两个数
# 你可以假设每个输入只对应一种答案,且同样的元素不能被重复利用.
# 实例:
# 给定 nums = [2,7,11,15],target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0,1]

"""
class Solution
    def twoSum(self,nums,target):
        :type nums:list[int]
        :type target:int
        :rtype:list[int]
"""
class Solution:
    def twoSum(self,nums,target):
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] + nums[j] == target:
        #             return [j,i]
        # else:
        #     return "查找失败"

        d = {}
        for i in range(len(nums)):
            j = target -nums[i]
            if j in d.keys():
                res = [d[j], i]
                break
            d[nums[i]] = i
        return res



sun = Solution()
print(sun.twoSum([3,3,3],6))
