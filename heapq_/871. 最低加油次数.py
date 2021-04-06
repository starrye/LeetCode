# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/6 3:59 下午
@file: 871. 最低加油次数.py
@desc: 
"""
import heapq
from typing import List
"""
汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。
沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。
假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。
当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。


示例 1：

输入：target = 1, startFuel = 1, stations = []
输出：0
解释：我们可以在不加油的情况下到达目的地。
示例 2：

输入：target = 100, startFuel = 1, stations = [[10,100]]
输出：-1
解释：我们无法抵达目的地，甚至无法到达第一个加油站。
示例 3：

输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
输出：2
解释：
我们出发时有 10 升燃料。
我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
我们沿途在1两个加油站停靠，所以返回 2 。
 

提示：

1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
"""


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 1/边界条件
        if stations:
            if startFuel < stations[0][0]:
                return -1
        else:
            if startFuel < target:
                return -1
            else:
                return 0

        # 2/优先级队列 中心思想:(并非真实存起来)每次先把油存起来，等到油不够到下一个目的地时，找到曾路过加油站中 油最多的加～
        heap = []
        ans = 0
        # 当前油量
        current_fuel = startFuel
        last_loc = 0
        for index, value in enumerate(stations):
            # 将油扔对堆里，注意python里面heapq是小顶堆，我们其实需要的是最大值 所以这里将它变为负数存储
            heapq.heappush(heap, -value[1])

            # 从上一个位置到当前位置的距离(主要用来计算油耗)
            distance = value[0] - last_loc
            last_loc = value[0]
            current_fuel -= distance

            # 如果当前油不能走到下一个位置(这里需要注意 是否下个位置为target, 否则就越界了)
            while current_fuel < (stations[index+1][0] - value[0] if index != len(stations) - 1 else target - stations[-1][0]):
                # 没有油了
                if not heap:
                    return -1
                # 路过加油站汇中 油量最多的
                max_fuel = heapq.heappop(heap)
                # 这里的 -= 其实对应上面说的 油量负数存储
                current_fuel -= max_fuel
                ans += 1

        return ans


a = Solution().minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]])
print(a)
assert Solution().minRefuelStops(999, 1000, [[5,100],[997,100],[998,100]]) == 0
assert Solution().minRefuelStops(1, 1, []) == 0
assert Solution().minRefuelStops(100, 1, [[10, 100]]) == -1
assert Solution().minRefuelStops(100, 1, []) == -1
