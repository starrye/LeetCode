# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 13. 机器人的运动范围.py
@Author: liuwz
@time: 2022/1/10 11:24 上午
@desc: 
"""
from collections import deque


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        Q = deque()
        Q.append([0, 0])
        visit = set()
        visit.add((0, 0))
        ans = 1
        while Q:
            x, y = Q.popleft()
            for n_x, n_y in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0 <= n_x < m and 0 <= n_y < n and self.dightsum(n_x, n_y) <= k and (n_x, n_y) not in visit:
                    Q.append([n_x, n_y])
                    visit.add((n_x, n_y))
                    ans += 1
        return ans
                
    def dightsum(self, x, y):
        result = 0
        while x:
            result += x % 10
            x //= 10
        while y:
            result += y % 10
            y //= 10
        return result

a = Solution().movingCount(11, 8, 16)
print(a)