# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
class Solution(object):
    def maxSubArray(self, nums):
        #当前和
        sum = 0
        #当前最大和
        max_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        return max_sum
a = Solution()
print(a.maxSubArray([5,-12,7,1,-1]))


