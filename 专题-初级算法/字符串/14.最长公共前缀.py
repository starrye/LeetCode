# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:所有输入只包含小写字母 a-z 。
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # s = ""
        # if len(strs) == 0:
        #     return ''
        # for i in zip(*strs):
        #     if len(set(i)) == 1:
        #         s += i[0]
        #     else:
        #         return s
        # return s
# a = Solution()
# print(a.longestCommonPrefix(['']))

#
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for x, y in enumerate(shortest):
            print(x,y)
            for s in strs:
                if s[x] != y:
                    return shortest[:x]
        return shortest
a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))

