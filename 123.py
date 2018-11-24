nums=[1,3,5,6]
target = 4
low = 0
high = len(nums)
while low <= high:
    mid = (low+high)//2
    if target <nums[mid]:
        high = mid-1
    elif target > nums[mid]:
        low = mid+1
    else:
        print(mid)
else:
    print(low)
