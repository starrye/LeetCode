#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 207. 课程表.py
@time: 2020/8/4 10:09
@desc: 
"""
from typing import List
"""
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
 
示例 1:

输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        from collections import deque
        # 入度数组(列表，保存所有课程的依赖课程总数)
        in_degree_list = [0] * numCourses
        # 关系表(字典，保存所有课程与依赖课程关系)
        relation_dict = defaultdict(list)
        for i in prerequisites:
            # 保存课程初始入度值
            in_degree_list[i[0]] += 1
            # 添加依赖它的后续课程
            relation_dict[i[1]].append(i[0])
        queue = deque()
        for i in range(len(in_degree_list)):
            # 入度为0的课程入列
            if in_degree_list[i] == 0:
                queue.append(i)
        # 队列只存储入度为0的课程，也就是可以直接选修的课程
        while queue:
            current = queue.popleft()
            # 选修课程-1
            numCourses -= 1
            relation_list = relation_dict[current]
            # 如果有依赖此课程的后续课程则更新入度
            if relation_list:
                for i in relation_list:
                    in_degree_list[i] -= 1
                    # 后续课程除去当前课程无其他依赖课程则丢入队列
                    if in_degree_list[i] == 0:
                        queue.append(i)
        return numCourses == 0

a = Solution().canFinish()