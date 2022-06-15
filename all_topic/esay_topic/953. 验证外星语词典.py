# encoding: utf-8
"""
@Project ：
@File: 953. 验证外星语词典.py
@Author: liuwz
@time: 2022/5/17 11:09
@desc: 
"""
from typing import List

""":cvar
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

 

示例 1：

输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
示例 2：

输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
输出：false
解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
示例 3：

输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
输出：false
解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（更多信息）。
 

提示：

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
在 words[i] 和 order 中的所有字符都是英文小写字母。
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # words_sort = sorted(words, key=lambda x: [order.index(i) for i in x])
        # return words_sort == words
        order_index = {v: -i for i,v in enumerate(order)}
        from functools import cmp_to_key

        def comp_by_order(s1, s2):
            n = 0
            while n < len(s1) and n < len(s2):
                if order_index[s1[n]] > order_index[s2[n]]:
                    return -1
                elif order_index[s1[n]] < order_index[s2[n]]:
                    return 1
                n += 1
            # 在前缀元素一致的情况下，s1长度>s2长度 则s1"较小"
            if n < len(s1):return 1
            else:return -1

        words_sort = sorted(words, key=cmp_to_key(comp_by_order))
        return words_sort == words

a = Solution().isAlienSorted(["apple","app"],"worldabcefghijkmnpqstuvxyz")
print(a)
b = Solution().isAlienSorted(["app","apple"],"worldabcefghijkmnpqstuvxyz")
print(b)
