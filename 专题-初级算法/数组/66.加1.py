# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # temp = 1
        # for i in range(len(digits)-1,-1,-1):
        #     digits[i] += temp
        #     if digits[i] == 10:
        #         digits[i] = 0
        #         temp = 1
        #     else:
        #         temp = 0
        # if temp == 1:
        #     digits.insert(0,1)
        # return digits
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        ans = [0]*(len(digits)+1)
        ans[0] = 1
        return ans


a = Solution().plusOne([9,9,9])
print(a)
