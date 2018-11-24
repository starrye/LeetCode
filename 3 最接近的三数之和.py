# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
# 使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
nums = [-1,2,1,-4]
target = 1
close_num = 0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)-1):
                nums_sum = nums[i] + nums[j] + nums[k]
                if close_num == 0:
                    close_num = nums_sum - target
                else:
                    if nums_sum - target < close_num :
                        close_num = nums_sum - target
print(nums_sum)
