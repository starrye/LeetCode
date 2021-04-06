# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/6 5:31 下午
@file: 295. 数据流的中位数.py
@desc: 
"""
import heapq
from typing import List
"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        维护大顶堆 与 小顶堆
        要点：
        1/大顶堆和小顶堆的元素个数相差不能超过1 且大顶堆小于等于小顶堆
        2/大顶堆的最大元素需要小于小顶堆的最小元素
        3/返回时判断如果长度不等 则直接返回小顶堆的根 否则返回 大顶堆与小顶堆的根的平均值
        """
        self.max_heap = []
        self.min_heap = []
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:

        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        # 0 <= 保证小顶堆的元素个数 - 大顶堆的元素个数 <= 1
        if len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        # 如果元素个数相同 则返回大顶堆根和小顶堆根的均值 否则返回小顶堆的根
        return self.min_heap[0] if len(self.max_heap) < len(self.min_heap) else (self.min_heap[0] + self.max_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()