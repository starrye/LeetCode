# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/1 4:06 下午
@file: 1696. 跳跃游戏 VI.py
@desc: 
"""
from collections import deque
from typing import List

"""
给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1, i + k)] 包含 两个端点的任意位置。
你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。
请你返回你能得到的 最大得分 。
 

示例 1：

输入：nums = [1,-1,-2,4,-7,3], k = 2
输出：7
解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。
示例 2：

输入：nums = [10,-5,-2,4,0,3], k = 3
输出：17
解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。
示例 3：

输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
输出：0
 
提示：
 1 <= nums.length, k <= 105
-104 <= nums[i] <= 104
"""

# 单调队列+动态规划


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = deque()
        dp = [0] * len(nums)
        for index, num in enumerate(nums):
            # 判断是否超过规定范围
            if index - k > 0:
                # 此处的判断->弹出真正该弹出的元素 此话怎讲？
                # 因为这里是单调递减队列 当前队列里有 3 2 1 然后要入队4 把三个都弹出去 此时队列里只有一个4 再入队一个2 本来需要弹出第一个3 但是由于他已经被弹出去了 不能再弹了
                # 如果没有这个判断 无脑弹第一个元素 就会把范围内的较大元素弹出去
                if queue and queue[0] == dp[index - k - 1]:
                    queue.popleft()
            # 队列头就是最大元素 没有元素则取0
            current_max = queue[0] if queue else 0
            # dp 表示当前位置的最大值 他需要从 当前范围内的最大值 + 当前位置的值
            dp[index] = current_max + num

            # 维护队列是单调递减的核心代码
            # 这里为什么引入单调队列 (假如不引入 那么刚才的current_max 就需要每次都从 max(dp[i-k], dp[i-k+1],.... dp[i-1]) + nums[i] 太多重复计算
            # 可以维护一个单调队列在O(1)时间内取得最大值)
            while queue and queue[-1] < dp[index]:
                queue.pop()
            queue.append(dp[index])
        return dp[-1]


a = Solution().maxResult([10,-5,-2,4,0,3], 3)
print(a)



