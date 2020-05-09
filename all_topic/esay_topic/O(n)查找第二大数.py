def the_second_big_num(arr):
    a = arr[0]
    b = a
    for i in range(len(arr)):
        if arr[i] > a:
            b = a
            a = arr[i]
        else:
            if arr[i] >b:
                b = arr[i]
    return b
yoyo = the_second_big_num([0,1,4,5,3,8])
print(yoyo)