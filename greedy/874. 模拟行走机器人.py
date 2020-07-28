#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 874. 模拟行走机器人.py
@time: 2020/7/27 16:08
@desc: 
"""
from typing import List
"""
机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
-2：向左转 90 度
-1：向右转 90 度
1 <= x <= 9：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物。

第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。

 

示例 1：

输入: commands = [4,-1,3], obstacles = []
输出: 25
解释: 机器人将会到达 (3, 4)
示例 2：

输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出: 65
解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
 
提示：
0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
答案保证小于 2 ^ 31
"""


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 初始位置
        current_loc = [0, 0]
        # 坐标偏移量
        dx, dy = 0, 1
        # 初始位置
        direction = "up"
        # 结果
        ans = 0
        # 障碍物列表转化为集合 因为判断位置是否在列表中时间为O(n) 而判断是否在集合中为O(1)
        obstacles = set(map(tuple, obstacles))
        for i in commands:
            # 移动
            if i > 0:
                for _ in range(i):
                    # 判断下一步是否会遇到障碍物
                    if (current_loc[0] + dx, current_loc[1] + dy) in obstacles:
                        break
                    current_loc[0] += dx
                    current_loc[1] += dy
                    ans = max(ans, current_loc[0] ** 2 + current_loc[1] ** 2)
            # 转向-右
            elif i == -1:
                # 当前往上(北)
                if direction == "up":
                    direction = "right"
                    dx, dy = 1, 0
                # 当前往下(南)
                elif direction == "down":
                    direction = "left"
                    dx, dy = -1, 0
                # 当前往东(右)
                elif direction == "right":
                    direction = "down"
                    dx, dy = 0, -1
                # 当前往西(左)
                elif direction == "left":
                    direction = "up"
                    dx, dy = 0, 1

            # 转向-左
            # 和转向-右 相反
            else:
                # 当前往上(北)
                if direction == "up":
                    direction = "left"
                    dx, dy = -1, 0
                # 当前往下(南)
                elif direction == "down":
                    direction = "right"
                    dx, dy = 1, 0
                # 当前往东(右)
                elif direction == "right":
                    direction = "up"
                    dx, dy = 0, 1
                # 当前往西(左)
                elif direction == "left":
                    direction = "down"
                    dx, dy = 0, -1
        return ans


a = Solution().robotSim([4,-1,4,-2,4], [[2, 4]])
print(a)





