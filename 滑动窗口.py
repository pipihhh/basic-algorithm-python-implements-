from 双向链表 import DoublyLinkList


class SlidingWindow(object):
    def __init__(self, lst):
        self._queue = DoublyLinkList()
        self._list = lst
        self._right = -1
        self._left = -1

    def sliding_right(self):
        if self._left <= self._right < len(self._list) - 1:
            self._right += 1
            self._append(self._right)

    def sliding_left(self):
        if self._right > self._left >= -1:
            self._left += 1
            self._pop(self._left)

    def _append(self, val):
        if self._queue.tail is not None:
            while self._queue.tail is not None and self._list[self._queue.tail] <= self._list[val] and self._queue.tail < val:
                self._queue.right_pop()
            self._queue.right_push(val)
            return
        self._queue.right_push(val)

    def _pop(self, val):
        if self._queue.tail is not None:
            if self._queue.head == val:
                self._queue.left_pop()
            elif self._queue.tail == val:
                self._queue.right_pop()

    @property
    def max(self):
        return self._list[self._queue.head]

    @property
    def max_index(self):
        return self._queue.head


if __name__ == '__main__':
    a = SlidingWindow([4, 3, 5, 4, 3, 3, 6, 7])
    a.sliding_right()
    a.sliding_right()
    a.sliding_right()
    ret = [a.max, ]
    count = 5
    while count:
        a.sliding_right()
        a.sliding_left()
        ret.append(a.max)
        count -= 1
    print(ret)
