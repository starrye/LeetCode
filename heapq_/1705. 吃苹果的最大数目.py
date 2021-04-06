# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/6 2:44 下午
@file: 1705. 吃苹果的最大数目.py
@desc: 
"""
import heapq
from typing import List
"""
有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。
你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。
给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。
 

示例 1：

输入：apples = [1,2,3,5,2], days = [3,2,1,4,2]
输出：7
解释：你可以吃掉 7 个苹果：
- 第一天，你吃掉第一天长出来的苹果。
- 第二天，你吃掉一个第二天长出来的苹果。
- 第三天，你吃掉一个第二天长出来的苹果。过了这一天，第三天长出来的苹果就已经腐烂了。
- 第四天到第七天，你吃的都是第四天长出来的苹果。
示例 2：

输入：apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
输出：5
解释：你可以吃掉 5 个苹果：
- 第一天到第三天，你吃的都是第一天长出来的苹果。
- 第四天和第五天不吃苹果。
- 第六天和第七天，你吃的都是第六天长出来的苹果。
 

提示：

apples.length == n
days.length == n
1 <= n <= 2 * 104
0 <= apples[i], days[i] <= 2 * 104
只有在 apples[i] = 0 时，days[i] = 0 才成立
"""

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # 优先级队列
        heap = []
        ans = 0
        n = len(apples)
        # 当前天数
        day = 0
        # 如果还有苹果在长 或者 还有苹果未烂
        while day < n or heap:
            # 今天长了多少苹果
            count = apples[day] if day < n else 0
            # 坏的日子
            bad = day + (days[day] if day < n else 0)
            heapq.heappush(heap, [bad, count])

            # 剔除掉队列里已经烂掉的苹果 因为heap小顶堆元素 是 距离当前最快坏的苹果 如果他没烂 那么剩下的苹果肯定都没烂
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            if heap:
                # 弹出小顶堆元素，吃最可能坏的苹果 做最有营养的人
                cur = heapq.heappop(heap)
                # 苹果数目-1
                cur[1] -= 1
                ans += 1
                # 如果还有苹果未坏 则继续扔到堆里
                if cur[1] > 0:
                    heapq.heappush(heap, cur)
            day += 1
        return ans

a = Solution().eatenApples([1,2,3,5,2], [3,2,1,4,2])
print(a)
