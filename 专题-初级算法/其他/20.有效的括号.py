# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
# 输入: "()"
# 输出: true
# 示例 2:
# 输入: "()[]{}"
# 输出: true
# 示例 3:
# 输入: "(]"
# 输出: false
# 示例 4:
# 输入: "([)]"
# 输出: false
# 示例 5:
# 输入: "{[]}"
# 输出: true

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack = []
        # balanced = True
        # index = 0
        # while index < len(s) and balanced:
        #     if s[index] in '([{':
        #         stack.append(s[index])
        #     else:
        #         if len(stack) == 0:
        #             balanced = False
        #         else:
        #             top = stack.pop()
        #             balanced = match(top,s[index])
        #     index += 1
        # if balanced and len(stack) == 0:
        #     return True
        # else:
        #     return False

# def match(open,close):
#     opens = '([{'
#     closes = ')]}'
#     return opens.index(open) == closes.index(close)

        stack = []
        dict_ = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in dict_.values():
                stack.append(i)
            else:
                if not stack or stack[-1] != dict_[i]:
                    return False
                stack.pop()
        return len(stack) == 0

s = Solution()
print(s.isValid('{{([][])}()}'))
print(s.isValid('[{()]'))