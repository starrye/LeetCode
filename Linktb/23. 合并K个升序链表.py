# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/2 4:25 下午
@file: 23. 合并K个升序链表.py
@desc: 
"""
import heapq
from typing import List

"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ListNode.__lt__ = lambda x, y: x.val < y.val
        heap = [x for x in lists if x]


        dummy = ListNode(None)
        head = dummy

        # 小顶堆
        heapq.heapify(heap)

        while heap:
            # 小节点取出和链表最后一个节点连接起来
            cur = heapq.heappop(heap)
            head.next = cur
            head = head.next

            if cur.next:
                heapq.heappush(heap, cur.next)

        return dummy.next
