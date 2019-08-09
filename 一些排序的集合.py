import random, copy
from collections import OrderedDict


class ManySort(object):
    def __init__(self, arr):
        self._arr = arr
        self.length = len(arr)

    @property
    def ret(self):
        return self._arr

    def choose_sort(self):
        for i in range(self.length):
            for j in range(i, self.length):
                if self._arr[i] > self._arr[j]:
                    self._arr[i], self._arr[j] = self._arr[j], self._arr[i]

    def bubble_sort(self):
        flag = True
        for i in range(self.length):
            flag = True
            for j in range(self.length-i-1):
                if self._arr[j] > self._arr[j+1]:
                    flag = False
                    self._arr[j], self._arr[j+1] = self._arr[j+1], self._arr[j]
            if flag:
                break

    def insert_sort(self):
        sorted_index = 0
        cur = 1
        disordered_index = self.length - 1
        while cur <= disordered_index:
            tmp_index = sorted_index
            cur_val = self._arr[cur]
            while cur_val < self._arr[tmp_index] and tmp_index >= 0:
                self._arr[tmp_index], self._arr[tmp_index + 1] = self._arr[tmp_index + 1], self._arr[tmp_index]
                tmp_index -= 1
            cur += 1
            sorted_index += 1

    def quick_sort(self, start, end):
        if start < end:
            less, more = self._quick_partition(start, end)
            self.quick_sort(start, less)
            self.quick_sort(more, end)

    def _quick_partition(self, start, end):
        less = start - 1
        more = end + 1
        cur = start
        rand = random.randint(start, end)
        num = self._arr[rand]
        while cur < more:
            if self._arr[cur] < num:
                self._arr[cur], self._arr[less + 1] = self._arr[less + 1], self._arr[cur]
                less += 1
                cur += 1
            elif self._arr[cur] > num:
                self._arr[cur], self._arr[more - 1] = self._arr[more - 1], self._arr[cur]
                more -= 1
            else:
                cur += 1
        return less, more


# l = list(range(10))
# random.shuffle(l)
# print(l)
# a = ManySort(l)
# a.quick_sort(0, 9)
# print(a.ret)

def test():
    arr1 = list(range(20))
    random.shuffle(arr1)
    arr2 = copy.deepcopy(arr1)
    arr3 = copy.deepcopy(arr1)
    a = ManySort(arr2)
    a.insert_sort()
    arr3.sort()
    if arr3 != a.ret:
        print(arr1)
        print(a.ret)
        print(arr3)
        import time
        time.sleep(5)
import copy

arr1 = list(range(5000))
# random.shuffle(arr1)
arr1.reverse()
arr2 = copy.deepcopy(arr1)
arr3 = copy.deepcopy(arr1)
# a = ManySort(arr1)
# a.bubble_sort()
# print(a.ret)
import time
a = ManySort(arr1)
t = time.time()
a.quick_sort(0, 4999)
print(time.time() - t)

