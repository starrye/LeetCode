# encoding: utf-8
"""
@Project ：
@File: 467. 环绕字符串中唯一的子字符串.py
@Author: liuwz
@time: 2022/5/25 10:57
@desc: 
"""


""":cvar
把字符串 s 看作是 “abcdefghijklmnopqrstuvwxyz” 的无限环绕字符串，所以 s 看起来是这样的：

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...." . 
现在给定另一个字符串 p 。返回 s 中 唯一 的 p 的 非空子串 的数量 。 

 

示例 1:

输入: p = "a"
输出: 1
解释: 字符串 s 中只有一个"a"子字符。
示例 2:

输入: p = "cac"
输出: 2
解释: 字符串 s 中的字符串“cac”只有两个子串“a”、“c”。.
示例 3:

输入: p = "zab"
输出: 6
解释: 在字符串 s 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。
 

提示:

1 <= p.length <= 105
p 由小写英文字母构成


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/unique-substrings-in-wraparound-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 前期一直纠结于怎么去重 类似zabecde
# 理解  遍历时 保持更新 以每个字符作为结尾的连续字串 最大长度  ！
# 创建26字母数组 保存以每个字母结尾的最长连续字串长度
# max(count[ord(p[i]) - 97], cur_len)
# 例如zadecde 在第一次得到e时 更新长度为2(de) 在第二次得到e时更新长度为3(cde) 则以e结尾的字符串就是3个 cde de e 自然就去重了

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        if n == 1:
            return 1
        count = [0] * 26
        cur_len = 0
        for i in range(n):
            # 连续
            if i > 0 and ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i-1]) - ord(p[i]) == 25:
                cur_len += 1
            # 不连续
            else:
                cur_len = 1
            count[ord(p[i]) - 97] = max(count[ord(p[i]) - 97], cur_len)
        ans = 0
        for i in count:
            ans += i
        return ans

a = Solution().findSubstringInWraproundString("zab")
print(a)