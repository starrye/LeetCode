# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 案例:
# s = "leetcode"
# 返回 0.
# s = "loveleetcode",
# 返回 2.
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # list1 = list(set(s))
        # # 排序为了后面遍历时获取的是第一个唯一字符
        # list1.sort(key=s.index)
        # for each in list1:
        #     if s.count(each) == 1:
        #         return s.index(each)
        # return -1
        check = []
        for i in 'abcdefghigklmnopqrstuvwxyz':
            if s.find(i) != -1 and s.find(i) == s.rfind(i):
                check.append(s.find(i))
        return min(check) if len(check) != 0 else -1
a = Solution()
print(a.firstUniqChar('leetcode'))