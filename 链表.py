class SingleNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkList(object):
    __slots__ = ("_head", "_tail", "_length")
    __len__ = lambda self: self._length

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def create_link_list_by_iter(self, iterable):
        iterable = iter(iterable)
        node = SingleNode(iterable.__next__())
        self._length = 1
        tmp = node
        for i in iterable:
            node.next = SingleNode(i)
            node = node.next
            self._length += 1
        self._tail = node
        self._head = tmp

    def is_empty(self):
        return self._length == 0

    def extends(self, iterable):
        if self.is_empty():
            raise RuntimeError("链表为空")
        iterable = iter(iterable)
        for i in iterable:
            node = SingleNode(i)
            self._tail.next = node
            self._tail = self._tail.next
            self._length += 1

    def _create_if_head_not_exist(self, node):
        if not self._head:
            self._tail.next = node
            self._tail = self._tail.next
            self._head = node
            return True
        return False

    def right_push(self, val):
        node = SingleNode(val)
        self._length += 1
        if not self._create_if_head_not_exist(node):
            self._tail.next = node
            self._tail = self._tail.next

    def left_push(self, val):
        node = SingleNode(val)
        self._length += 1
        if not self._create_if_head_not_exist(node):
            node.next = self._head
            self._head = node

    def left_pop(self):
        if self._head:
            tmp = self._head
            val = tmp.val
            self._head = self._head.next
            del tmp
            self._length -= 1
            return val
        raise LookupError("链表为空")


a = SingleLinkList()
a.create_link_list_by_iter([1, 2, 3, 4, 5, 6])
print(a.left_pop())
a.left_push(1)
a.left_push(1)
a.left_push(1)
print(a.left_pop())
print(len(a))
