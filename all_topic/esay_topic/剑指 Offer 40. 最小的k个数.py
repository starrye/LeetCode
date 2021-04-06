# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/2 11:07 上午
@file: 剑指 Offer 40. 最小的k个数.py
@desc: 
"""
from typing import List

"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
"""

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        import heapq
        # python只自带了小顶堆，我们需要取最小的k个数，则将队列里的数全部取负数放进去，然后找出最大的k个数 最后再取反即可

        # heap = [-num for num in arr]  # creates an empty heap
        #
        # heapq.heapify(heap)  # transforms list into a heap, in-place, in linear timea
        #
        # for i in range(k, len(arr)):
        #     heapq.heappop(heap)  # pops the smallest item from the heap
        # return [-num for num in heap]

        """nsmallest   :   Find the n smallest elements in a dataset."""
        return heapq.nsmallest(k, arr)


a = Solution().getLeastNumbers([3,2,1], 2)
print(a)