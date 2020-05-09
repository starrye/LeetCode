# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 说明：
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # list1 = []
        # if len(nums1) < len(nums2):
        #     for i in nums1:
        #         if i in nums2:
        #             list1.append(i)
        # else:
        #     for i in nums2:
        #         if i in nums1:
        #             nums1.remove(i)
        #             list1.append(i)
        # return list(set(list1))

        list = set(nums1) & set(nums2)
        l = []
        for i in list:
            l += [i] * min(nums1.count(i),nums2.count(i))
        return l
a = Solution()
print(a.intersect([3,1,2],[1,1]))