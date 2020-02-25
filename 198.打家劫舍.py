# 示例 1:
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划简化版
        last_max = 0
        curr_max = 0
        for i in nums:
            curr_max, last_max= max(last_max+i,curr_max), curr_max
        return curr_max

        # 动态规划思想详细版
        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return max(nums[0], nums[1])
        # import numpy as np
        # opt = np.zeros(len(nums))
        # len_arr = len(nums)
        # opt[0] = nums[0]
        # opt[1] = max(nums[0],nums[1])
        # for i in range(2, len_arr):
        #     opt[i] = max(opt[i-2]+nums[i], opt[i-1])
        # return int(opt[-1])

a = Solution()
print(a.rob([2,7,9,3,1]))