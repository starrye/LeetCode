# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]
# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
class Solution:
    def intersection(self, nums1, nums2):
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
        #             list1.append(i)
        # return list(set(list1))

        nums1 = set(nums1)
        nums2 = set(nums2)
        list1 = nums1 & nums2
        return list(list1)
a = Solution()
print(a.intersection([4,9,5], [9,4,9,8,4]))