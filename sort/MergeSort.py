#归并排序
#sort过程
#将数组拆分调用merge函数返回已经排序好的数组
#merge过程
#设定两个指针，最初位置分别为两个已经排序序列的起始位置；
#比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
#重复步骤 3 直到某一指针达到序列尾；
#将另一序列剩下的所有元素直接复制到合并序列尾。

class MergeSort(object):
    # 拆分 再调用 合并过程
    def sort(self, list):
        if len(list) <= 1:
            return list
        mid = len(list) // 2
        # 调试一下
        left = MergeSort().sort(list[:mid])
        print("-----1",left)
        right = MergeSort().sort(list[mid:])
        print("-----2",right)
        return MergeSort().merge(left, right)
    #合并过程
    def merge(self, left, right):
        new_list = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                new_list.append(left[i])
                i += 1
            else:
                new_list.append(right[j])
                j += 1
        new_list.extend(left[i:])
        new_list.extend(right[j:])
        return new_list

a = MergeSort().sort([1, 4, 2, 6, 3, 7])
print(a)