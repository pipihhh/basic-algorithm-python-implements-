from random import randint


class RandomPool(object):
    """
    此池子实现了3个方法分别为，insert，delete，getrandom，时间复杂度均为big O(1)
    """
    def __init__(self):
        self.__content = {}
        self.__map = {}
        self._size = 0

    def insert(self, val):
        self.__content[val] = self._size
        self.__map[self._size] = val
        self._size += 1

    def delete(self, val):
        if self._size:
            self._size -= 1
            self.__map[self.__content[val]] = self.__map[self._size]
            self.__content[self.__map[self._size]] = self.__content[val]
            del self.__content[val]
            del self.__map[self._size]

    def get_random(self):
        if self._size:
            rand = randint(0, self._size-1)
            return self.__map[rand]
        raise KeyError("哈希表为空")

    def __iter__(self):
        return iter(self.__content.keys())


a = RandomPool()
for i in range(10):
    a.insert(str(i))
a.delete("5")
a.delete("6")
a.delete("7")
list(a)
