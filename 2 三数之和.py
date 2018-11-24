# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找
# 出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
nums = [-1,0,1,2,-1,-4]
num = []
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)-1):
        for k in range (j+1,len(nums)-1):
            if nums[i] + nums[j] + nums[k] == 0:
                if len(num) == 0 :
                    num.append([nums[i], nums[j], nums[k]])
                else:
                    l = 0
                    for l in range(len(num)):
                        if nums[i] in num[l] and nums[j] in num[l] and nums[k] in num[l]:
                            break
                        else:
                            num.append([nums[i],nums[j],nums[k]])
print(num)


