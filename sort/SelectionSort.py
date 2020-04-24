#选择排序
"""
从小到大
从数组中找到最小的元素放置排序数组的开头
从余下的数组中找到最小的元素放置已排序数组的末尾
重复第二步
"""
class SelectionSort():
    def selectionsort(self,list):
        #需要数组长度-1次排序过程
        for i in range(len(list)-1):
            min = i
            for j in range(i,len(list)):
                if list[j] < list[min]:
                    min = j
            if i != min:
                list[i],list[min] = list[min],list[i]
        return list
a = SelectionSort().selectionsort([1,4,2,5,3])
print(a)