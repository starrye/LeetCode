# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组char[]的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用O(1)的额外空间解决这一问题。
# 你可以假设数组中的所有字符都是ASCII码表中的可打印字符。
# 示例
# 输入：["h", "e", "l", "l", "o"]
# 输出：["o", "l", "l", "e", "h"]

class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
a = Solution()
print(a.reverseString(["h","e","l","l","o"]))