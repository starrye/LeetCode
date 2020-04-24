# 快速排序
#从数组挑出一个元素作为基准，重新排列数组，小的在左边 大的在右边，则排序完该数就位于数列的中间位置（理论中间） #分而治之
class QuickSort(object):

    def quick_sort(self,arr):  # 长度初始化
        return self.q_sort(arr, 0, len(arr)-1)

    def q_sort(self, arr, left, right):
        if left < right:
            partitionIndex = self.partion(arr, left, right)
            self.q_sort(arr, left, partitionIndex-1)
            self.q_sort(arr, partitionIndex+1, right)
        return arr

    def partion(self, arr, left, right):
        pivot = arr[left]
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        return left


a = QuickSort().quick_sort([1, 4, 2, 6, 3, 7])
print(a)
