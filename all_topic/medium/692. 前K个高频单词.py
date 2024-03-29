# encoding: utf-8
"""
@author: liuwz
@time: 2021/4/2 2:00 下午
@file: 692. 前K个高频单词.py
@desc: 
"""
from typing import List

"""
给一非空的单词列表，返回前 k 个出现次数最多的单词。
返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
示例 1：
输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
 
示例 2：
输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
 
注意：

假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。
 

扩展练习：

尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决
"""
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # c_words = Counter(words)
        # heap = [(-c, w) for w, c in c_words.items()]
        # heapq.heapify(heap)
        # return [heapq.heappop(heap)[1] for _ in range(k)]

        return [x[0] for x in heapq.nsmallest(k, Counter(words).items(), key=lambda x:(-x[1], x[0]))]


a = Solution().topKFrequent(["love", "i", "leetcode", "i", "love", "coding"], 2)
print(a)