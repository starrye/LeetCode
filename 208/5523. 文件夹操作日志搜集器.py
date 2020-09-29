#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 5523. 文件夹操作日志搜集器.py
@time: 2020/9/27 10:30
@desc: 
"""
from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:

            if log == "../":
                if ans != 0:
                    ans -= 1
                else:
                    continue
            elif log == "./":
                continue
            else:
                ans += 1
            print('--log:%s' % log)
            print(ans)
        return ans if ans >= 0 else 0

a  = Solution().minOperations(["./","wz4/","../","mj2/","../","../","ik0/","il7/"])
print(a)