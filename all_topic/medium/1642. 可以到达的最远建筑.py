# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/6 2:12 下午
@file: 1642. 可以到达的最远建筑.py
@desc: 
"""
import heapq
from typing import List

"""
给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。
你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。
当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：
如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块
如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。
 

示例 1：


输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
输出：4
解释：从建筑物 0 出发，你可以按此方案完成旅程：
- 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
- 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
- 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
- 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
无法越过建筑物 4 ，因为没有更多砖块或梯子。
示例 2：

输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
输出：7
示例 3：

输入：heights = [14,3,19,3], bricks = 17, ladders = 0
输出：3
 

提示：

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
"""

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heaq = []

        """
        优先级队列 记录 落差
        每当遇到 转块不够用时，选取最大的落差 替换成梯子 使用  然后把砖块还回去
        """
        for index, height in enumerate(heights):
            if index == 0:
                continue
            # 这里的cur_height 是负数，因为python里面的堆是小顶堆， 而我们需要返回最大落差 则取负数即可
            cur_height = heights[index-1] - height
            if cur_height < 0:
                heapq.heappush(heaq, cur_height)
                # 这里看似是 += 其实 cur_height是负数 其实bricks是在减少的一个过程
                bricks += cur_height
                # 砖块不够用
                if bricks < 0:
                    # 如果有梯子
                    if ladders:
                        # 最大落差用梯子替换
                        max_height = heapq.heappop(heaq)
                        # 增加砖块
                        bricks -= max_height
                        # 梯子数量-1
                        ladders -= 1
                    # 没有梯子同时砖块不够
                    else:
                        # 这层上不去
                        return index - 1
        return len(heights) - 1


a= Solution().furthestBuilding([4,2,7,6,9,14,12], 5, 1)
print(a)


