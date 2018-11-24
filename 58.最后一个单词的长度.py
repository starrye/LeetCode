# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 示例:
#
# 输入: "Hello World"
# 输出: 5
# class Solution:
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         str = ''
#         count = 0
#         for i in s[::-1]:
#             if str != '' and i == ' ':
#                 return count
#             if i != ' ':
#                 count = count + 1
#         return count
# a = Solution()
# print(a.lengthOfLastWord("  day  "))

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        else:
            arr = s.split()
            if len(arr) > 0:
                return len(arr[-1])
            else:
                return 0
a = Solution()
print(a.lengthOfLastWord("  "))

