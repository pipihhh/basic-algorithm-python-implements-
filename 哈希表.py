from 链表 import SingleLinkList
from threading import Thread


class HashMap(object):
    """
    使用动态扩容的哈希表，每次扩容 起一个线程在后台执行，不阻塞
    """
    def __init__(self, start_size=10):
        self._max_size = start_size
        self._map_size = 0
        self._content = [None for _ in range(self._max_size)]
        self._hash = lambda obj, num: hash(num) % (obj._max_size - 1)

    def put(self, key, val):
        h_val = self._hash(self, key)
        if self._content[h_val] is None:
            self._content[h_val] = SingleLinkList()
        self._content[h_val].right_push((key, val))
        self._map_size += 1
        self._check_size()

    def _check_size(self):
        if self._map_size > self._max_size * 0.7:
            thread = Thread(target=HashMap._expansion, args=(self, ))
            thread.run()

    def get(self, key):
        h_val = self._hash(self, key)
        link_list = self._content[h_val]
        if link_list is not None:
            for k, v in link_list:
                if key == k:
                    return v
        return None

    def items(self):
        for i in self._content:
            if i is not None:
                for val in i:
                    yield val

    def _expansion(self):
        new_map = HashMap(2*self._max_size)
        for i in self.items():
            new_map.put(i[0], i[1])
        self._max_size = new_map._max_size
        self._content = new_map._content


if __name__ == '__main__':

    a = HashMap()
    for i in range(1, 10, 102):
        a.put(i, str(i))

    for i in range(1, 10, 102):
        a.get(i)
