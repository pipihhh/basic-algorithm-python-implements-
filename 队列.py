class MyQueue(object):
    def __init__(self, count):
        self.__content = [None for _ in range(count)]
        self._count = count
        self._size = 0
        self._start = 0
        self._end = 0

    @property
    def is_empty(self):
        return self._size == 0

    @property
    def is_full(self):
        return self._size == self._count

    def __len__(self):
        return self._size

    def push(self, element):
        if not self.is_full:
            self.__content[self._end] = element
            self._end = 0 if self._end == self._count - 1 else self._end + 1
            self._size += 1
            return
        raise IndexError("队列已满，无法再次填充元素")

    def pop(self):
        if not self.is_empty:
            tmp = self._start
            self._start = 0 if self._start == self._count - 1 else self._start + 1
            self._size -= 1
            return self.__content[tmp]
        raise IndexError("队列为空，无法弹出元素")

    def peek(self):
        if self.is_empty:
            raise IndexError("队列为空，无法查看队首元素")
        return self.__content[self._start]

