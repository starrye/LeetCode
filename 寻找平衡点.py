def balance_point(thy_list):
    num = len(thy_list)
    if num >= 3:
        for i in range(num):
            if i == 0:
                pass
            else:
                list1 = thy_list[:i]
                list2 = thy_list[i+1:]
                sum1 = sum(list1)
                sum2 = sum(list2)
                if sum1 == sum2:
                    return '平衡点:%d' % thy_list[i]
        return '无平衡点'
    else:
        return  '列表长度不够！'
print(balance_point([1, 3, 5, 7, 8, 25, 4, 20]))