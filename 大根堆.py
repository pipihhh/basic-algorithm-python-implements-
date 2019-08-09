class BigHeap(object):
    def __init__(self, arr):
        try:
            self._arr = list(arr)
            self._length = len(arr)
            self._build_heap()
        except TypeError as e:
            raise TypeError("必须传入可迭代对象")

    def insert(self, num):
        self._arr.append(num)
        self._heap_insert(self._length)
        self._length += 1

    def _build_heap(self):
        for i in range(self._length):
            self._heap_insert(i)

    def _heap_insert(self, index):
        while self._arr[index] > self._arr[abs(index-1)//2]:
            self._arr[index], self._arr[abs(index-1)//2] = self._arr[abs(index-1)//2], self._arr[index]
            index = abs(index-1) // 2

    def _heapify(self, index, size):
        left = index * 2 + 1
        while left < size:
            largest_index = left+1 if left + 1 < size and self._arr[left] < self._arr[left+1] else left
            if self._arr[index] > self._arr[largest_index]:
                break
            self._arr[index], self._arr[largest_index] = self._arr[largest_index], self._arr[index]
            index = largest_index
            left = 2 * largest_index + 1

    def pop(self):
        self._arr[-1], self._arr[0] = self._arr[0], self._arr[-1]
        self._length -= 1
        self._heapify(0, self._length)
        return self._arr.pop()

    def sort(self):
        for i in range(self._length-1, -1, -1):
            self._arr[0], self._arr[i] = self._arr[i], self._arr[0]
            self._heapify(0, i)

    def __getitem__(self, item):
        return self._arr[item]

    def __str__(self):
        return str(self._arr)

    def __len__(self):
        return self._length


h = BigHeap([1, 5, 4, 3, 2, 1])
h.insert(10)
h.sort()
print(len(h))
