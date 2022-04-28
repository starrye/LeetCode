# encoding: utf-8
"""
@Project ： 
@File: 剑指 Offer 21.调整数组顺序使奇数位于偶数前面.py
@Author: liuwz
@time: 2022/3/30 12:00 下午
@desc: 
"""
from typing import List

""":cvar
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

0 <= nums.length <= 50000
0 <= nums[i] <= 10000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd, even = len(nums) - 1, 0
        while odd >= even:
            while odd > even and not nums[odd] & 1:
                odd -= 1
            while odd > even and nums[even] & 1:
                even += 1
            nums[odd], nums[even] = nums[even], nums[odd]
            odd -= 1
            even += 1
        return nums


a = Solution().exchange([1,3,5])
print(a)
