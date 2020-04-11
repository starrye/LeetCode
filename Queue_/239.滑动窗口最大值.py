#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 239.滑动窗口最大值.py
@time: 2020/4/11 18:34
@desc: 
"""
"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
进阶：
你能在线性时间复杂度内解决此题吗？
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 双端队列
        result = []
        import collections
        queue = collections.deque()
        for index, value in enumerate(nums):
            # 前k-1个元素只存储并始终确保最大元素位于对头，并不存储最大元素
            if index < k-1:
                # 具体做法：当队列不为空且当前元素大于队尾元素，则弹出队尾元素，直到队列为空或者小于队尾元素，则将元素携带索引入队
                while queue and value > queue[-1][1]:
                    queue.pop()
                queue.append([index, value])
                continue
            else:
                # 对比前 首先确保对头也就是最大值是否已经滑出窗口
                if queue and index - queue[0][0] == k:
                    queue.popleft()
                while queue and value > queue[-1][1]:
                    queue.pop()
                queue.append([index, value])
            # 最大元素写入列表中
            result.append(queue[0][1])
        return result


a = Solution().maxSlidingWindow([1], 1)
print(a)
