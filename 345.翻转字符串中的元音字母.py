# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 示例 1:
# 输入: "hello"
# 输出: "holle"
# 示例 2:
# 输入: "leetcode"
# 输出: "leotcede"

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [i for i in s]
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and s[i] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                i += 1
            while i < j and s[j] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                j -= 1
            if i < j and s[i] != s[j]:
                s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
a = Solution()
print(a.reverseVowels("hello"))