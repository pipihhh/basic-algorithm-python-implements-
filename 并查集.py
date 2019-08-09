class UnionFindSet(object):
    """
    并查集，使用O(1)的时间来判断两个元素是否在同一个集合中。
    """
    def __init__(self, iterable):
        self._size = {}
        self._parent = {}
        for i in iterable:
            self._parent[i] = i
            self._size[i] = 1

    def is_same_set(self, item1, item2):
        if self._parent.get(item1) is None or self._parent.get(item2) is None:
            return False
        item1_father = self._get_father(item1)
        item2_father = self._get_father(item2)
        return item1_father == item2_father

    def _get_father(self, item):
        stack = [item, ]
        while stack:
            item = stack[-1]
            tmp = self._parent[item]
            if tmp == item:
                stack.pop()
                for i in stack:
                    self._parent[i] = tmp
                break
            else:
                stack.append(tmp)
        return item

    def union(self, item1, item2):
        if self._parent.get(item1) is None or self._parent.get(item2) is None:
            return
        item1_father = self._get_father(item1)
        item2_father = self._get_father(item2)
        if self._size[item1_father] >= self._size[item2_father]:
            self._parent[item2] = item1_father
            self._size[item1_father] += self._size[item2_father]
            self._size.pop(item2_father)
        else:
            self._parent[item1] = item2_father
            self._size[item2_father] += self._size[item1_father]
            self._size.pop(item1_father)


a = UnionFindSet([1, 2, 3, 4, 5])
a.union(2, 3)
print(a.is_same_set(2, 3))
