#希尔排序
#定义增量 根据这个增量把数组分为n个小组
#每个小组利用倒叙直接插入排序 把最小的数放置小组的开头
#随着增量的逐渐降低,每组的长度越来越长
#最后增量降至为1 则为简单插入排序过程
class ShellSort():
    def shellsort(self,list):
        m = len(list)
        n = 0
        grep = (m+n) // 2
        while grep > 0:
            for i in range(grep,m):
                j = i
                #倒叙对比 把每组最小的放到最前面
                while (j-grep) >= 0:
                    if list[j] - list[j-grep] < 0:
                        list[j],list[j-grep] = list[j-grep],list[j]
                        j = j-grep
                    else:
                        break
            #步长缩小一半
            grep //= 2
        return list
a = ShellSort().shellsort([4,6,2,1,4,7])
print(a)
