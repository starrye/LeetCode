#插入排序
#将第一个元素看作已排序元素，第二个元素到最后一个元素看作未排序元素
#遍历未排序元素，将其与已排序元素对比 放到合适的位置，若相同放置相同元素的后面

class InsertSort():
    def insetsort(self,list):
        #从1开始
        for i in range(1,len(list)):
            #未排序中要插入的数据 --> 当前数
            tmp = list[i]
            #遍历从已排序的最右边开始 也就是i-1的位置
            #若当前数比遍历的数小 则依次把数往后移动
            for j in range(i-1,-1,-1):
                if list[j] > tmp:
                    #依次往后移动
                    list[j],list[j+1] = tmp,list[j]

        return list
a = InsertSort().insetsort([1,5,3,2,5])
print(a)

