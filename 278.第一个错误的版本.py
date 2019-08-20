# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
# 示例:
# 给定 n = 5，并且 version = 4 是第一个错误的版本。
# 调用 isBadVersion(3) -> false
# 调用 isBadVersion(5) -> true
# 调用 isBadVersion(4) -> true
#
# 所以，4 是第一个错误的版本。
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        hight = n

        while low < hight:
            mid = (low + hight) // 2
            if isBadVersion(mid):
                hight = mid
            else:
                low = mid+1
        return hight



