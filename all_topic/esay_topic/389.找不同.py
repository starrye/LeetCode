class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # s = list(s)
        # for i in t:
        #     if i in s:
        #         s.remove(i)
        #     else:
        #         return i

        # 异或！！！！！！
        result = 0
        for i in range(len(s)):
            result ^= ord(s[i]) - 97
        print(result)
        for i  in range(len(t)):
            result ^= ord(t[i]) - 97  # ord将字符转化为对应的数字
        return chr(result + 97)  # chr将对应的数字转化为字符，'a'对应的数字是97
a = Solution()
print(a.findTheDifference("abcde","abcdef"))