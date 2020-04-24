#冒泡排序
"""
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
"""
class BubbleSort ():
    def bubblesort(self,list):
        for i in range(len(list)):
            #初始化一个标志位表示此次是否进行了循环，若否 则排序完成
            noexchange = True
            for j in range(len(list)-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
                    noexchange = False
            if noexchange:
                break
        return list
a = BubbleSort().bubblesort([4,1,2,4,5])
print(a)
