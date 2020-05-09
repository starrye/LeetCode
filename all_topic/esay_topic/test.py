import bisect
import re


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
a = [1,1]
a.remove(1)
print(a)

