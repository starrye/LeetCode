import bisect
import re
from typing import List

# stack_ = ["c","r","o","k","c"]
#
# print(stack_.index("c"))
# print(stack_)



# class Solution:
#     def stoneGameIII(self, s) -> str:
#         su = 0
#         dp = [0]*(len(s)+3)
#         for i in range(len(s)-1, -1, -1):
#             su += s[i]
#             # 对手最优情况下获取最少的石子数
#             cho = min(dp[i+1], dp[i+2], dp[i+3])
#             dp[i] = su - cho
#    #    print(dp)
#         if dp[0]+dp[0] < su:
#             return "Bob"
#         elif dp[0]+dp[0]>su:

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         prefix, suffix, max_so_far = 0, 0, float('-inf')
#         for i in range(len(nums)):
#             prefix = (prefix or 1) * nums[i]
#             suffix = (suffix or 1) * nums[~i]
#             max_so_far = max(max_so_far, prefix, suffix)
#         return max_so_far
#
#
# a = Solution().maxProduct([-1, 2, -1, 5, -2, 2, 10])
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        i = 0
        while i < (length - 2):
            for j in range(i+1, length-1):
                va = 0 - nums[i] - nums[j]
                if va in nums[j+1:]:
                    temp_ = sorted([va, nums[i], nums[j]])
                    if temp_ not in result:
                        result.append(temp_)
            i += 1
        return result

a = Solution().threeSum([-1, 0,1])
print(a)
